<template>
  <div class="pt-20 min-h-screen">
    <div class="max-w-6xl mx-auto px-6 py-12">
      <!-- Login Form -->
      <div v-if="!isAuthenticated" class="max-w-md mx-auto">
        <div class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-8">
          <h1 class="text-2xl font-bold text-zinc-900 dark:text-white mb-6 text-center">Admin Login</h1>
          
          <form @submit.prevent="login">
            <div class="mb-6">
              <label for="password" class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Password</label>
              <input
                v-model="password"
                type="password"
                id="password"
                required
                class="w-full px-4 py-3 bg-light-bg dark:bg-dark-bg border border-light-border dark:border-dark-border rounded-xl text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-transparent"
                placeholder="Enter admin password"
              />
            </div>
            
            <p v-if="loginError" class="text-red-500 text-sm mb-4">{{ loginError }}</p>
            
            <Button type="submit" variant="primary" size="lg" fullWidth :loading="loggingIn">
              <Lock class="w-5 h-5" />
              Login
            </Button>
          </form>
        </div>
      </div>

      <!-- Admin Dashboard -->
      <div v-else>
        <div class="flex items-center justify-between mb-8">
          <h1 class="text-2xl font-bold text-zinc-900 dark:text-white">Blog Admin</h1>
          <div class="flex gap-4">
            <Button variant="primary" @click="showCreateModal = true">
              <Plus class="w-5 h-5" />
              New Post
            </Button>
            <Button variant="ghost" @click="logout">
              <LogOut class="w-5 h-5" />
              Logout
            </Button>
          </div>
        </div>

        <!-- Posts List -->
        <div v-if="loadingPosts" class="flex justify-center py-12">
          <Loader2 class="w-8 h-8 text-brand-500 animate-spin" />
        </div>

        <div v-else-if="posts.length === 0" class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-12 text-center">
          <FileText class="w-12 h-12 text-zinc-400 mx-auto mb-4" />
          <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-2">No posts yet</h2>
          <p class="text-zinc-600 dark:text-zinc-400 mb-6">Create your first blog post to get started.</p>
          <Button variant="primary" @click="showCreateModal = true">
            <Plus class="w-5 h-5" />
            Create Post
          </Button>
        </div>

        <div v-else class="space-y-4">
          <div 
            v-for="post in posts" 
            :key="post.id"
            class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-6 flex items-center justify-between"
          >
            <div class="flex-1">
              <div class="flex items-center gap-3 mb-2">
                <h3 class="text-lg font-semibold text-zinc-900 dark:text-white">{{ post.title }}</h3>
                <span 
                  :class="post.published ? 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400' : 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400'"
                  class="px-2 py-0.5 text-xs font-medium rounded-full"
                >
                  {{ post.published ? 'Published' : 'Draft' }}
                </span>
              </div>
              <p class="text-sm text-zinc-600 dark:text-zinc-400">{{ post.excerpt }}</p>
              <div class="flex items-center gap-4 mt-2 text-xs text-zinc-500">
                <span>{{ formatDate(post.created_at) }}</span>
                <span v-if="post.tags.length">Tags: {{ post.tags.join(', ') }}</span>
              </div>
            </div>
            <div class="flex items-center gap-2 ml-4">
              <Button variant="ghost" size="sm" @click="editPost(post)">
                <Edit class="w-4 h-4" />
              </Button>
              <Button variant="ghost" size="sm" @click="confirmDelete(post)">
                <Trash2 class="w-4 h-4 text-red-500" />
              </Button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Create/Edit Modal -->
    <div v-if="showCreateModal || showEditModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-light-card dark:bg-dark-card rounded-xl w-full max-w-4xl max-h-[90vh] overflow-y-auto">
        <div class="p-6 border-b border-light-border dark:border-dark-border flex items-center justify-between">
          <h2 class="text-xl font-semibold text-zinc-900 dark:text-white">
            {{ showEditModal ? 'Edit Post' : 'Create New Post' }}
          </h2>
          <button @click="closeModal" class="text-zinc-400 hover:text-zinc-600 dark:hover:text-zinc-200">
            <X class="w-6 h-6" />
          </button>
        </div>
        
        <form @submit.prevent="savePost" class="p-6 space-y-6">
          <!-- Title -->
          <div>
            <label class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Title</label>
            <input
              v-model="postForm.title"
              type="text"
              required
              class="w-full px-4 py-3 bg-light-bg dark:bg-dark-bg border border-light-border dark:border-dark-border rounded-xl text-zinc-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500"
              placeholder="Post title"
            />
          </div>

          <!-- Excerpt -->
          <div>
            <label class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Excerpt</label>
            <textarea
              v-model="postForm.excerpt"
              required
              rows="2"
              class="w-full px-4 py-3 bg-light-bg dark:bg-dark-bg border border-light-border dark:border-dark-border rounded-xl text-zinc-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500 resize-none"
              placeholder="Brief description of the post"
            ></textarea>
          </div>

          <!-- Content -->
          <div>
            <label class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Content (Markdown)</label>
            <textarea
              v-model="postForm.content"
              required
              rows="12"
              class="w-full px-4 py-3 bg-light-bg dark:bg-dark-bg border border-light-border dark:border-dark-border rounded-xl text-zinc-900 dark:text-white font-mono text-sm focus:outline-none focus:ring-2 focus:ring-brand-500 resize-none"
              placeholder="Write your post content in Markdown..."
            ></textarea>
          </div>

          <!-- Tags -->
          <div>
            <label class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Tags (comma-separated)</label>
            <input
              v-model="tagsInput"
              type="text"
              class="w-full px-4 py-3 bg-light-bg dark:bg-dark-bg border border-light-border dark:border-dark-border rounded-xl text-zinc-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500"
              placeholder="backend, python, fastapi"
            />
          </div>

          <!-- Featured Image URL -->
          <div>
            <label class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Featured Image URL</label>
            <input
              v-model="postForm.featured_image"
              type="url"
              class="w-full px-4 py-3 bg-light-bg dark:bg-dark-bg border border-light-border dark:border-dark-border rounded-xl text-zinc-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500"
              placeholder="https://example.com/image.jpg"
            />
          </div>

          <!-- Published Toggle -->
          <div class="flex items-center gap-3">
            <input
              v-model="postForm.published"
              type="checkbox"
              id="published"
              class="w-5 h-5 rounded border-zinc-300 text-brand-500 focus:ring-brand-500"
            />
            <label for="published" class="text-sm font-medium text-zinc-700 dark:text-zinc-300">Publish immediately</label>
          </div>

          <!-- Actions -->
          <div class="flex justify-end gap-4 pt-4 border-t border-light-border dark:border-dark-border">
            <Button type="button" variant="outline" @click="closeModal">Cancel</Button>
            <Button type="submit" variant="primary" :loading="saving">
              {{ showEditModal ? 'Update Post' : 'Create Post' }}
            </Button>
          </div>
        </form>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div v-if="showDeleteModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-light-card dark:bg-dark-card rounded-xl p-6 max-w-md w-full">
        <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-4">Delete Post?</h2>
        <p class="text-zinc-600 dark:text-zinc-400 mb-6">Are you sure you want to delete "{{ postToDelete?.title }}"? This action cannot be undone.</p>
        <div class="flex justify-end gap-4">
          <Button variant="outline" @click="showDeleteModal = false">Cancel</Button>
          <Button variant="primary" class="!bg-red-500 hover:!bg-red-600" @click="deletePost" :loading="deleting">
            Delete
          </Button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { Lock, Plus, LogOut, Edit, Trash2, X, Loader2, FileText } from 'lucide-vue-next'
import Button from '../components/Button.vue'
import axios from 'axios'

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || ''
const API = `${BACKEND_URL}/api`

// Auth state
const isAuthenticated = ref(false)
const password = ref('')
const loginError = ref('')
const loggingIn = ref(false)

// Posts state
const posts = ref([])
const loadingPosts = ref(false)

// Modal state
const showCreateModal = ref(false)
const showEditModal = ref(false)
const showDeleteModal = ref(false)
const editingPost = ref(null)
const postToDelete = ref(null)
const saving = ref(false)
const deleting = ref(false)

// Form state
const postForm = ref({
  title: '',
  excerpt: '',
  content: '',
  featured_image: '',
  published: false
})
const tagsInput = ref('')

const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'short', 
    day: 'numeric' 
  })
}

const getAuthHeader = () => ({
  auth: {
    username: 'admin',
    password: localStorage.getItem('adminPassword') || ''
  }
})

const login = async () => {
  loggingIn.value = true
  loginError.value = ''
  
  try {
    const response = await axios.post(`${API}/admin/login`, { password: password.value })
    if (response.data.success) {
      isAuthenticated.value = true
      localStorage.setItem('adminPassword', password.value)
      await fetchPosts()
    }
  } catch (error) {
    loginError.value = 'Invalid password'
  } finally {
    loggingIn.value = false
  }
}

const logout = () => {
  isAuthenticated.value = false
  localStorage.removeItem('adminPassword')
  password.value = ''
}

const fetchPosts = async () => {
  loadingPosts.value = true
  try {
    const response = await axios.get(`${API}/admin/posts`, getAuthHeader())
    posts.value = response.data
  } catch (error) {
    console.error('Failed to fetch posts:', error)
    if (error.response?.status === 401) {
      logout()
    }
  } finally {
    loadingPosts.value = false
  }
}

const editPost = (post) => {
  editingPost.value = post
  postForm.value = {
    title: post.title,
    excerpt: post.excerpt,
    content: post.content,
    featured_image: post.featured_image || '',
    published: post.published
  }
  tagsInput.value = post.tags.join(', ')
  showEditModal.value = true
}

const closeModal = () => {
  showCreateModal.value = false
  showEditModal.value = false
  editingPost.value = null
  postForm.value = {
    title: '',
    excerpt: '',
    content: '',
    featured_image: '',
    published: false
  }
  tagsInput.value = ''
}

const savePost = async () => {
  saving.value = true
  
  const tags = tagsInput.value
    .split(',')
    .map(t => t.trim())
    .filter(t => t.length > 0)
  
  const postData = {
    ...postForm.value,
    tags
  }
  
  try {
    if (showEditModal.value && editingPost.value) {
      await axios.put(`${API}/blog/posts/${editingPost.value.id}`, postData, getAuthHeader())
    } else {
      await axios.post(`${API}/blog/posts`, postData, getAuthHeader())
    }
    await fetchPosts()
    closeModal()
  } catch (error) {
    console.error('Failed to save post:', error)
    alert('Failed to save post. Please try again.')
  } finally {
    saving.value = false
  }
}

const confirmDelete = (post) => {
  postToDelete.value = post
  showDeleteModal.value = true
}

const deletePost = async () => {
  if (!postToDelete.value) return
  
  deleting.value = true
  try {
    await axios.delete(`${API}/blog/posts/${postToDelete.value.id}`, getAuthHeader())
    await fetchPosts()
    showDeleteModal.value = false
    postToDelete.value = null
  } catch (error) {
    console.error('Failed to delete post:', error)
    alert('Failed to delete post. Please try again.')
  } finally {
    deleting.value = false
  }
}

onMounted(() => {
  // Check if already authenticated
  const savedPassword = localStorage.getItem('adminPassword')
  if (savedPassword) {
    password.value = savedPassword
    login()
  }
})
</script>
