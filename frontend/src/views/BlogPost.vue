<template>
  <div class="pt-20">
    <div class="max-w-4xl mx-auto px-6 py-20">
      <!-- Loading -->
      <div v-if="loading" class="flex justify-center py-20">
        <Loader2 class="w-8 h-8 text-brand-500 animate-spin" />
      </div>

      <!-- Not Found -->
      <div v-else-if="!post" class="text-center py-20">
        <h1 class="text-2xl font-bold text-zinc-900 dark:text-white mb-4">Post not found</h1>
        <router-link to="/blog">
          <Button variant="primary">Back to Blog</Button>
        </router-link>
      </div>

      <!-- Post Content -->
      <article v-else class="animate-fade-in">
        <!-- Back Button -->
        <router-link to="/blog" class="inline-flex items-center gap-2 text-zinc-600 dark:text-zinc-400 hover:text-brand-500 dark:hover:text-brand-400 mb-8 transition-colors duration-200">
          <ArrowLeft class="w-4 h-4" />
          Back to Blog
        </router-link>

        <!-- Tags -->
        <div v-if="post.tags.length" class="flex flex-wrap gap-2 mb-4">
          <span 
            v-for="tag in post.tags" 
            :key="tag"
            class="px-3 py-1 text-sm font-medium bg-brand-100 dark:bg-brand-900/30 text-brand-700 dark:text-brand-400 rounded-full"
          >
            {{ tag }}
          </span>
        </div>

        <!-- Title -->
        <h1 class="text-3xl md:text-4xl font-bold text-zinc-900 dark:text-white mb-4">
          {{ post.title }}
        </h1>

        <!-- Meta -->
        <div class="flex items-center gap-4 text-sm text-zinc-500 dark:text-zinc-500 mb-8">
          <span class="flex items-center gap-2">
            <Calendar class="w-4 h-4" />
            {{ formatDate(post.created_at) }}
          </span>
          <span class="flex items-center gap-2">
            <Clock class="w-4 h-4" />
            {{ readingTime }} min read
          </span>
        </div>

        <!-- Featured Image -->
        <div v-if="post.featured_image" class="rounded-xl overflow-hidden mb-8">
          <img 
            :src="post.featured_image" 
            :alt="post.title"
            class="w-full h-auto"
          />
        </div>

        <!-- Content -->
        <div class="prose prose-zinc dark:prose-invert max-w-none" v-html="renderedContent"></div>
      </article>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { ArrowLeft, Calendar, Clock, Loader2 } from 'lucide-vue-next'
import Button from '../components/Button.vue'
import axios from 'axios'

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || ''
const API = `${BACKEND_URL}/api`

const route = useRoute()
const post = ref(null)
const loading = ref(true)

const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  })
}

const readingTime = computed(() => {
  if (!post.value) return 0
  const words = post.value.content.split(/\s+/).length
  return Math.ceil(words / 200)
})

// Simple markdown renderer
const renderedContent = computed(() => {
  if (!post.value) return ''
  let content = post.value.content
  
  // Headers
  content = content.replace(/^### (.*$)/gim, '<h3 class="text-xl font-semibold mt-8 mb-4">$1</h3>')
  content = content.replace(/^## (.*$)/gim, '<h2 class="text-2xl font-semibold mt-10 mb-4">$1</h2>')
  content = content.replace(/^# (.*$)/gim, '<h1 class="text-3xl font-bold mt-12 mb-6">$1</h1>')
  
  // Bold and italic
  content = content.replace(/\*\*\*(.*?)\*\*\*/g, '<strong><em>$1</em></strong>')
  content = content.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
  content = content.replace(/\*(.*?)\*/g, '<em>$1</em>')
  
  // Code blocks
  content = content.replace(/```([\s\S]*?)```/g, '<pre class="bg-zinc-100 dark:bg-zinc-800 rounded-lg p-4 overflow-x-auto my-4"><code>$1</code></pre>')
  content = content.replace(/`([^`]+)`/g, '<code class="bg-zinc-100 dark:bg-zinc-800 px-1.5 py-0.5 rounded text-sm">$1</code>')
  
  // Links
  content = content.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" class="text-brand-500 hover:text-brand-600 underline" target="_blank" rel="noopener">$1</a>')
  
  // Lists
  content = content.replace(/^\* (.*$)/gim, '<li class="ml-4">$1</li>')
  content = content.replace(/^- (.*$)/gim, '<li class="ml-4">$1</li>')
  content = content.replace(/^\d+\. (.*$)/gim, '<li class="ml-4 list-decimal">$1</li>')
  
  // Paragraphs
  content = content.replace(/\n\n/g, '</p><p class="mb-4">')
  content = '<p class="mb-4">' + content + '</p>'
  
  // Clean up empty paragraphs
  content = content.replace(/<p class="mb-4"><\/p>/g, '')
  content = content.replace(/<p class="mb-4">(<h[1-6])/g, '$1')
  content = content.replace(/(<\/h[1-6]>)<\/p>/g, '$1')
  content = content.replace(/<p class="mb-4">(<pre)/g, '$1')
  content = content.replace(/(<\/pre>)<\/p>/g, '$1')
  
  return content
})

onMounted(async () => {
  try {
    const response = await axios.get(`${API}/blog/posts/${route.params.slug}`)
    post.value = response.data
  } catch (error) {
    console.error('Failed to fetch blog post:', error)
  } finally {
    loading.value = false
  }
})
</script>

<style>
.prose h1, .prose h2, .prose h3 {
  color: inherit;
}
.prose p {
  color: inherit;
  opacity: 0.8;
}
.prose a {
  color: #0ea5e9;
}
.prose code {
  color: inherit;
}
</style>
