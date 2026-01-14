from fastapi import FastAPI, APIRouter, HTTPException, Depends, status, UploadFile, File
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
import secrets
import resend
import base64
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import List, Optional
import uuid
from datetime import datetime, timezone
from slugify import slugify

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ.get('DB_NAME', 'aakash_portfolio')]

# Resend configuration
resend.api_key = os.environ.get('RESEND_API_KEY', '')
NOTIFICATION_EMAIL = os.environ.get('NOTIFICATION_EMAIL', 'work.aakashm@gmail.com')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

# Create the main app
app = FastAPI(title="Aakash Malik Portfolio API")

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Security
security = HTTPBasic()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ==================== MODELS ====================

# Contact Form Models
class ContactMessage(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: EmailStr
    message: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    read: bool = False

class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    message: str

# Blog Post Models
class BlogPost(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    slug: str
    excerpt: str
    content: str  # Markdown content
    tags: List[str] = []
    featured_image: Optional[str] = None  # Base64 or URL
    published: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class BlogPostCreate(BaseModel):
    title: str
    excerpt: str
    content: str
    tags: List[str] = []
    featured_image: Optional[str] = None
    published: bool = False

class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    excerpt: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None
    featured_image: Optional[str] = None
    published: Optional[bool] = None

# Auth Models
class AdminLogin(BaseModel):
    password: str

class AuthResponse(BaseModel):
    success: bool
    message: str

# ==================== HELPER FUNCTIONS ====================

def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    """Verify admin credentials"""
    correct_password = secrets.compare_digest(credentials.password, ADMIN_PASSWORD)
    if not correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True

async def send_contact_notification(contact: ContactMessage):
    """Send email notification for new contact message"""
    try:
        params = {
            "from": "Portfolio Contact <onboarding@resend.dev>",
            "to": [NOTIFICATION_EMAIL],
            "subject": f"New Contact Form Message from {contact.name}",
            "html": f"""
            <h2>New Contact Form Submission</h2>
            <p><strong>Name:</strong> {contact.name}</p>
            <p><strong>Email:</strong> {contact.email}</p>
            <p><strong>Message:</strong></p>
            <p>{contact.message}</p>
            <hr>
            <p><small>Received at: {contact.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}</small></p>
            """,
        }
        email = resend.Emails.send(params)
        logger.info(f"Email notification sent: {email}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email notification: {e}")
        return False

# ==================== ROUTES ====================

@api_router.get("/")
async def root():
    return {"message": "Aakash Malik Portfolio API", "status": "running"}

# ---------- CONTACT FORM ROUTES ----------

@api_router.post("/contact", response_model=ContactMessage)
async def submit_contact_form(contact_data: ContactMessageCreate):
    """Submit a contact form message"""
    contact = ContactMessage(**contact_data.model_dump())
    
    # Save to database
    doc = contact.model_dump()
    doc['created_at'] = doc['created_at'].isoformat()
    await db.contact_messages.insert_one(doc)
    
    # Send email notification
    await send_contact_notification(contact)
    
    return contact

@api_router.get("/contact/messages", response_model=List[ContactMessage])
async def get_contact_messages(is_admin: bool = Depends(verify_admin)):
    """Get all contact messages (admin only)"""
    messages = await db.contact_messages.find({}, {"_id": 0}).sort("created_at", -1).to_list(100)
    
    for msg in messages:
        if isinstance(msg.get('created_at'), str):
            msg['created_at'] = datetime.fromisoformat(msg['created_at'])
    
    return messages

@api_router.put("/contact/messages/{message_id}/read")
async def mark_message_read(message_id: str, is_admin: bool = Depends(verify_admin)):
    """Mark a contact message as read"""
    result = await db.contact_messages.update_one(
        {"id": message_id},
        {"$set": {"read": True}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"success": True}

# ---------- BLOG ROUTES ----------

@api_router.get("/blog/posts", response_model=List[BlogPost])
async def get_blog_posts(published_only: bool = True):
    """Get all blog posts (published only for public, all for admin)"""
    query = {"published": True} if published_only else {}
    posts = await db.blog_posts.find(query, {"_id": 0}).sort("created_at", -1).to_list(100)
    
    for post in posts:
        if isinstance(post.get('created_at'), str):
            post['created_at'] = datetime.fromisoformat(post['created_at'])
        if isinstance(post.get('updated_at'), str):
            post['updated_at'] = datetime.fromisoformat(post['updated_at'])
    
    return posts

@api_router.get("/blog/posts/{slug}", response_model=BlogPost)
async def get_blog_post(slug: str):
    """Get a single blog post by slug"""
    post = await db.blog_posts.find_one({"slug": slug, "published": True}, {"_id": 0})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if isinstance(post.get('created_at'), str):
        post['created_at'] = datetime.fromisoformat(post['created_at'])
    if isinstance(post.get('updated_at'), str):
        post['updated_at'] = datetime.fromisoformat(post['updated_at'])
    
    return post

@api_router.post("/blog/posts", response_model=BlogPost)
async def create_blog_post(post_data: BlogPostCreate, is_admin: bool = Depends(verify_admin)):
    """Create a new blog post (admin only)"""
    # Generate slug from title
    base_slug = slugify(post_data.title)
    slug = base_slug
    counter = 1
    
    # Ensure unique slug
    while await db.blog_posts.find_one({"slug": slug}):
        slug = f"{base_slug}-{counter}"
        counter += 1
    
    post = BlogPost(
        **post_data.model_dump(),
        slug=slug
    )
    
    doc = post.model_dump()
    doc['created_at'] = doc['created_at'].isoformat()
    doc['updated_at'] = doc['updated_at'].isoformat()
    
    await db.blog_posts.insert_one(doc)
    return post

@api_router.put("/blog/posts/{post_id}", response_model=BlogPost)
async def update_blog_post(post_id: str, post_data: BlogPostUpdate, is_admin: bool = Depends(verify_admin)):
    """Update a blog post (admin only)"""
    # Get existing post
    existing = await db.blog_posts.find_one({"id": post_id}, {"_id": 0})
    if not existing:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Update fields
    update_data = {k: v for k, v in post_data.model_dump().items() if v is not None}
    update_data['updated_at'] = datetime.now(timezone.utc).isoformat()
    
    # Update slug if title changed
    if 'title' in update_data:
        base_slug = slugify(update_data['title'])
        slug = base_slug
        counter = 1
        while await db.blog_posts.find_one({"slug": slug, "id": {"$ne": post_id}}):
            slug = f"{base_slug}-{counter}"
            counter += 1
        update_data['slug'] = slug
    
    await db.blog_posts.update_one({"id": post_id}, {"$set": update_data})
    
    updated = await db.blog_posts.find_one({"id": post_id}, {"_id": 0})
    if isinstance(updated.get('created_at'), str):
        updated['created_at'] = datetime.fromisoformat(updated['created_at'])
    if isinstance(updated.get('updated_at'), str):
        updated['updated_at'] = datetime.fromisoformat(updated['updated_at'])
    
    return updated

@api_router.delete("/blog/posts/{post_id}")
async def delete_blog_post(post_id: str, is_admin: bool = Depends(verify_admin)):
    """Delete a blog post (admin only)"""
    result = await db.blog_posts.delete_one({"id": post_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"success": True, "message": "Post deleted"}

# ---------- ADMIN AUTH ROUTES ----------

@api_router.post("/admin/login", response_model=AuthResponse)
async def admin_login(login_data: AdminLogin):
    """Verify admin password"""
    if secrets.compare_digest(login_data.password, ADMIN_PASSWORD):
        return AuthResponse(success=True, message="Login successful")
    raise HTTPException(status_code=401, detail="Invalid password")

@api_router.get("/admin/posts", response_model=List[BlogPost])
async def get_admin_posts(is_admin: bool = Depends(verify_admin)):
    """Get all blog posts including unpublished (admin only)"""
    posts = await db.blog_posts.find({}, {"_id": 0}).sort("created_at", -1).to_list(100)
    
    for post in posts:
        if isinstance(post.get('created_at'), str):
            post['created_at'] = datetime.fromisoformat(post['created_at'])
        if isinstance(post.get('updated_at'), str):
            post['updated_at'] = datetime.fromisoformat(post['updated_at'])
    
    return posts

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
