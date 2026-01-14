<template>
  <div class="pt-20">
    <div class="max-w-4xl mx-auto px-6 py-20">
      <!-- Header -->
      <div class="mb-12 animate-fade-in">
        <h1 class="text-3xl md:text-4xl font-bold text-zinc-900 dark:text-white mb-4">Blog</h1>
        <p class="text-lg text-zinc-600 dark:text-zinc-400">Thoughts on engineering, systems, and technology</p>
        <div class="w-20 h-1 bg-brand-500 rounded-full mt-4"></div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex justify-center py-20">
        <Loader2 class="w-8 h-8 text-brand-500 animate-spin" />
      </div>

      <!-- No Posts -->
      <div v-else-if="posts.length === 0" class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-12 text-center animate-slide-up">
        <div class="p-4 rounded-full bg-brand-100 dark:bg-brand-900/30 w-fit mx-auto mb-6">
          <PenLine class="w-8 h-8 text-brand-600 dark:text-brand-400" />
        </div>
        <h2 class="text-2xl font-semibold text-zinc-900 dark:text-white mb-4">Writing coming soon</h2>
        <p class="text-zinc-600 dark:text-zinc-400 max-w-md mx-auto">
          I'm working on articles about backend systems, architecture patterns, and lessons learned from building production systems. Stay tuned!
        </p>
      </div>

      <!-- Blog Posts Grid -->
      <div v-else class="space-y-8 animate-slide-up">
        <article 
          v-for="post in posts" 
          :key="post.id"
          class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl overflow-hidden hover:border-brand-300 dark:hover:border-brand-700 transition-all duration-300 group"
        >
          <router-link :to="`/blog/${post.slug}`" class="block">
            <!-- Featured Image -->
            <div v-if="post.featured_image" class="aspect-video overflow-hidden">
              <img 
                :src="post.featured_image" 
                :alt="post.title"
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              />
            </div>
            
            <div class="p-6">
              <!-- Tags -->
              <div v-if="post.tags.length" class="flex flex-wrap gap-2 mb-3">
                <span 
                  v-for="tag in post.tags" 
                  :key="tag"
                  class="px-2 py-1 text-xs font-medium bg-brand-100 dark:bg-brand-900/30 text-brand-700 dark:text-brand-400 rounded-md"
                >
                  {{ tag }}
                </span>
              </div>
              
              <!-- Title -->
              <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-2 group-hover:text-brand-500 dark:group-hover:text-brand-400 transition-colors duration-200">
                {{ post.title }}
              </h2>
              
              <!-- Excerpt -->
              <p class="text-zinc-600 dark:text-zinc-400 mb-4 line-clamp-2">
                {{ post.excerpt }}
              </p>
              
              <!-- Meta -->
              <div class="flex items-center justify-between text-sm text-zinc-500 dark:text-zinc-500">
                <span>{{ formatDate(post.created_at) }}</span>
                <span class="flex items-center gap-1 text-brand-500 dark:text-brand-400 group-hover:gap-2 transition-all duration-200">
                  Read more
                  <ArrowRight class="w-4 h-4" />
                </span>
              </div>
            </div>
          </router-link>
        </article>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { PenLine, Loader2, ArrowRight } from 'lucide-vue-next'
import axios from 'axios'

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || ''
const API = `${BACKEND_URL}/api`

const posts = ref([])
const loading = ref(true)

const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  })
}

onMounted(async () => {
  try {
    const response = await axios.get(`${API}/blog/posts`)
    posts.value = response.data
  } catch (error) {
    console.error('Failed to fetch blog posts:', error)
  } finally {
    loading.value = false
  }
})
</script>
