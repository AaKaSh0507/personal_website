import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Experience from '../views/Experience.vue'
import Projects from '../views/Projects.vue'
import ProjectDetail from '../views/ProjectDetail.vue'
import TechStack from '../views/TechStack.vue'
import Blog from '../views/Blog.vue'
import BlogPost from '../views/BlogPost.vue'
import Resume from '../views/Resume.vue'
import Contact from '../views/Contact.vue'
import Admin from '../views/Admin.vue'

const routes = [
  { path: '/', name: 'Home', component: Home, meta: { title: 'Aakash Malik | Software Development Engineer' } },
  { path: '/about', name: 'About', component: About, meta: { title: 'About | Aakash Malik' } },
  { path: '/experience', name: 'Experience', component: Experience, meta: { title: 'Experience | Aakash Malik' } },
  { path: '/projects', name: 'Projects', component: Projects, meta: { title: 'Projects | Aakash Malik' } },
  { path: '/projects/:slug', name: 'ProjectDetail', component: ProjectDetail, meta: { title: 'Project | Aakash Malik' } },
  { path: '/tech-stack', name: 'TechStack', component: TechStack, meta: { title: 'Tech Stack | Aakash Malik' } },
  { path: '/blog', name: 'Blog', component: Blog, meta: { title: 'Blog | Aakash Malik' } },
  { path: '/blog/:slug', name: 'BlogPost', component: BlogPost, meta: { title: 'Blog | Aakash Malik' } },
  { path: '/resume', name: 'Resume', component: Resume, meta: { title: 'Resume | Aakash Malik' } },
  { path: '/contact', name: 'Contact', component: Contact, meta: { title: 'Contact | Aakash Malik' } },
  { path: '/admin', name: 'Admin', component: Admin, meta: { title: 'Admin | Aakash Malik' } }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    return { top: 0 }
  }
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Aakash Malik'
  next()
})

export default router
