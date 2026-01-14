#!/usr/bin/env python3
"""
Backend API Testing for Aakash Malik's Portfolio
Tests all backend APIs including contact form, blog posts, and admin functionality
"""

import requests
import json
import base64
from datetime import datetime
import sys
import os

# Get backend URL from frontend .env
BACKEND_URL = "https://aakash-engineer.preview.emergentagent.com/api"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "ssAY54^!"

class PortfolioAPITester:
    def __init__(self):
        self.base_url = BACKEND_URL
        self.session = requests.Session()
        self.test_results = []
        self.created_post_id = None
        
    def log_result(self, test_name, success, message, details=None):
        """Log test result"""
        status = "✅ PASS" if success else "❌ FAIL"
        result = {
            'test': test_name,
            'status': status,
            'message': message,
            'details': details or {}
        }
        self.test_results.append(result)
        print(f"{status}: {test_name} - {message}")
        if details and not success:
            print(f"   Details: {details}")
    
    def test_root_endpoint(self):
        """Test the root API endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/")
            if response.status_code == 200:
                data = response.json()
                if "Aakash Malik Portfolio API" in data.get("message", ""):
                    self.log_result("Root Endpoint", True, "API is running")
                    return True
                else:
                    self.log_result("Root Endpoint", False, "Unexpected response", data)
            else:
                self.log_result("Root Endpoint", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Root Endpoint", False, f"Connection error: {str(e)}")
        return False
    
    def test_contact_form_submission(self):
        """Test contact form submission"""
        try:
            contact_data = {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "message": "Hello! I'm interested in your portfolio and would like to discuss potential opportunities."
            }
            
            response = self.session.post(
                f"{self.base_url}/contact",
                json=contact_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                required_fields = ['id', 'name', 'email', 'message', 'created_at']
                if all(field in data for field in required_fields):
                    if data['name'] == contact_data['name'] and data['email'] == contact_data['email']:
                        self.log_result("Contact Form Submission", True, "Contact form submitted successfully")
                        return True
                    else:
                        self.log_result("Contact Form Submission", False, "Data mismatch in response", data)
                else:
                    self.log_result("Contact Form Submission", False, "Missing required fields", data)
            else:
                self.log_result("Contact Form Submission", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Contact Form Submission", False, f"Error: {str(e)}")
        return False
    
    def test_public_blog_posts(self):
        """Test getting public blog posts"""
        try:
            response = self.session.get(f"{self.base_url}/blog/posts")
            
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    self.log_result("Public Blog Posts", True, f"Retrieved {len(data)} blog posts")
                    return True
                else:
                    self.log_result("Public Blog Posts", False, "Response is not a list", data)
            else:
                self.log_result("Public Blog Posts", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Public Blog Posts", False, f"Error: {str(e)}")
        return False
    
    def test_blog_post_by_slug_not_found(self):
        """Test getting a non-existent blog post by slug"""
        try:
            response = self.session.get(f"{self.base_url}/blog/posts/non-existent-slug")
            
            if response.status_code == 404:
                self.log_result("Blog Post Not Found", True, "Correctly returned 404 for non-existent slug")
                return True
            else:
                self.log_result("Blog Post Not Found", False, f"Expected 404, got {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Blog Post Not Found", False, f"Error: {str(e)}")
        return False
    
    def test_admin_login_success(self):
        """Test admin login with correct password"""
        try:
            login_data = {"password": ADMIN_PASSWORD}
            
            response = self.session.post(
                f"{self.base_url}/admin/login",
                json=login_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success") is True and "Login successful" in data.get("message", ""):
                    self.log_result("Admin Login Success", True, "Admin login successful")
                    return True
                else:
                    self.log_result("Admin Login Success", False, "Unexpected response", data)
            else:
                self.log_result("Admin Login Success", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Admin Login Success", False, f"Error: {str(e)}")
        return False
    
    def test_admin_login_failure(self):
        """Test admin login with wrong password"""
        try:
            login_data = {"password": "wrongpassword"}
            
            response = self.session.post(
                f"{self.base_url}/admin/login",
                json=login_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 401:
                self.log_result("Admin Login Failure", True, "Correctly rejected wrong password")
                return True
            else:
                self.log_result("Admin Login Failure", False, f"Expected 401, got {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Admin Login Failure", False, f"Error: {str(e)}")
        return False
    
    def get_basic_auth_header(self):
        """Get Basic Auth header for admin requests"""
        credentials = f"{ADMIN_USERNAME}:{ADMIN_PASSWORD}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return {"Authorization": f"Basic {encoded_credentials}"}
    
    def test_admin_get_all_posts(self):
        """Test getting all posts (including unpublished) as admin"""
        try:
            headers = self.get_basic_auth_header()
            response = self.session.get(f"{self.base_url}/admin/posts", headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    self.log_result("Admin Get All Posts", True, f"Retrieved {len(data)} posts (including unpublished)")
                    return True
                else:
                    self.log_result("Admin Get All Posts", False, "Response is not a list", data)
            else:
                self.log_result("Admin Get All Posts", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Admin Get All Posts", False, f"Error: {str(e)}")
        return False
    
    def test_create_blog_post(self):
        """Test creating a new blog post as admin"""
        try:
            headers = self.get_basic_auth_header()
            headers["Content-Type"] = "application/json"
            
            post_data = {
                "title": "Test Blog Post - API Testing",
                "excerpt": "This is a test blog post created during API testing to verify CRUD operations.",
                "content": "# Test Blog Post\n\nThis is **markdown** content for testing purposes.\n\n## Features Tested\n\n- Blog post creation\n- Markdown rendering\n- Tag management\n\n*This post will be deleted after testing.*",
                "tags": ["test", "api", "automation"],
                "published": True
            }
            
            response = self.session.post(
                f"{self.base_url}/blog/posts",
                json=post_data,
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                required_fields = ['id', 'title', 'slug', 'content', 'created_at']
                if all(field in data for field in required_fields):
                    self.created_post_id = data['id']
                    self.log_result("Create Blog Post", True, f"Created post with ID: {self.created_post_id}")
                    return True
                else:
                    self.log_result("Create Blog Post", False, "Missing required fields", data)
            else:
                self.log_result("Create Blog Post", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Create Blog Post", False, f"Error: {str(e)}")
        return False
    
    def test_update_blog_post(self):
        """Test updating a blog post as admin"""
        if not self.created_post_id:
            self.log_result("Update Blog Post", False, "No post ID available for update test")
            return False
        
        try:
            headers = self.get_basic_auth_header()
            headers["Content-Type"] = "application/json"
            
            update_data = {
                "title": "Updated Test Blog Post - API Testing",
                "excerpt": "This is an updated test blog post to verify update functionality.",
                "tags": ["test", "api", "automation", "updated"]
            }
            
            response = self.session.put(
                f"{self.base_url}/blog/posts/{self.created_post_id}",
                json=update_data,
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('title') == update_data['title']:
                    self.log_result("Update Blog Post", True, f"Successfully updated post {self.created_post_id}")
                    return True
                else:
                    self.log_result("Update Blog Post", False, "Title not updated correctly", data)
            else:
                self.log_result("Update Blog Post", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Update Blog Post", False, f"Error: {str(e)}")
        return False
    
    def test_get_created_post_by_slug(self):
        """Test getting the created post by its slug"""
        if not self.created_post_id:
            self.log_result("Get Post by Slug", False, "No post created for slug test")
            return False
        
        try:
            # First get the post to find its slug
            headers = self.get_basic_auth_header()
            response = self.session.get(f"{self.base_url}/admin/posts", headers=headers)
            
            if response.status_code == 200:
                posts = response.json()
                created_post = next((p for p in posts if p['id'] == self.created_post_id), None)
                
                if created_post and 'slug' in created_post:
                    slug = created_post['slug']
                    
                    # Now test getting by slug
                    slug_response = self.session.get(f"{self.base_url}/blog/posts/{slug}")
                    
                    if slug_response.status_code == 200:
                        slug_data = slug_response.json()
                        if slug_data.get('id') == self.created_post_id:
                            self.log_result("Get Post by Slug", True, f"Successfully retrieved post by slug: {slug}")
                            return True
                        else:
                            self.log_result("Get Post by Slug", False, "Retrieved wrong post", slug_data)
                    else:
                        self.log_result("Get Post by Slug", False, f"HTTP {slug_response.status_code}", slug_response.text)
                else:
                    self.log_result("Get Post by Slug", False, "Could not find created post or slug")
            else:
                self.log_result("Get Post by Slug", False, f"Could not get posts: HTTP {response.status_code}")
        except Exception as e:
            self.log_result("Get Post by Slug", False, f"Error: {str(e)}")
        return False
    
    def test_delete_blog_post(self):
        """Test deleting a blog post as admin"""
        if not self.created_post_id:
            self.log_result("Delete Blog Post", False, "No post ID available for delete test")
            return False
        
        try:
            headers = self.get_basic_auth_header()
            
            response = self.session.delete(
                f"{self.base_url}/blog/posts/{self.created_post_id}",
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success') is True:
                    self.log_result("Delete Blog Post", True, f"Successfully deleted post {self.created_post_id}")
                    return True
                else:
                    self.log_result("Delete Blog Post", False, "Unexpected response", data)
            else:
                self.log_result("Delete Blog Post", False, f"HTTP {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Delete Blog Post", False, f"Error: {str(e)}")
        return False
    
    def test_unauthorized_admin_access(self):
        """Test that admin endpoints require authentication"""
        try:
            # Try to access admin posts without auth
            response = self.session.get(f"{self.base_url}/admin/posts")
            
            if response.status_code == 401:
                self.log_result("Unauthorized Admin Access", True, "Correctly blocked unauthorized access")
                return True
            else:
                self.log_result("Unauthorized Admin Access", False, f"Expected 401, got {response.status_code}", response.text)
        except Exception as e:
            self.log_result("Unauthorized Admin Access", False, f"Error: {str(e)}")
        return False
    
    def run_all_tests(self):
        """Run all API tests"""
        print(f"🚀 Starting API tests for: {self.base_url}")
        print("=" * 60)
        
        # Basic connectivity
        if not self.test_root_endpoint():
            print("❌ Cannot connect to API. Stopping tests.")
            return False
        
        # Public endpoints
        self.test_contact_form_submission()
        self.test_public_blog_posts()
        self.test_blog_post_by_slug_not_found()
        
        # Admin authentication
        self.test_admin_login_success()
        self.test_admin_login_failure()
        self.test_unauthorized_admin_access()
        
        # Admin blog management (CRUD operations)
        self.test_admin_get_all_posts()
        self.test_create_blog_post()
        self.test_update_blog_post()
        self.test_get_created_post_by_slug()
        self.test_delete_blog_post()
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for r in self.test_results if "✅" in r['status'])
        failed = sum(1 for r in self.test_results if "❌" in r['status'])
        
        print(f"Total Tests: {len(self.test_results)}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        
        if failed > 0:
            print("\n❌ FAILED TESTS:")
            for result in self.test_results:
                if "❌" in result['status']:
                    print(f"  - {result['test']}: {result['message']}")
        
        return failed == 0

if __name__ == "__main__":
    tester = PortfolioAPITester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)