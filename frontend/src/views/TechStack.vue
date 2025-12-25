<template>
  <div class="pt-20">
    <div class="max-w-6xl mx-auto px-6 py-20">
      <!-- Header -->
      <div class="mb-12 animate-fade-in">
        <h1 class="text-3xl md:text-4xl font-bold text-zinc-900 dark:text-white mb-4">Tech Stack</h1>
        <p class="text-lg text-zinc-600 dark:text-zinc-400">Technologies and tools I work with</p>
        <div class="w-20 h-1 bg-brand-500 rounded-full mt-4"></div>
      </div>

      <!-- Categories -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 animate-slide-up">
        <div v-for="category in categories" :key="category.title" class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-6 hover:border-brand-300 dark:hover:border-brand-700 transition-colors duration-300">
          <div class="flex items-center gap-3 mb-6">
            <div class="p-2 rounded-lg bg-brand-100 dark:bg-brand-900/30">
              <component :is="category.icon" class="w-5 h-5 text-brand-600 dark:text-brand-400" />
            </div>
            <h2 class="text-lg font-semibold text-zinc-900 dark:text-white">{{ category.title }}</h2>
          </div>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="item in category.items"
              :key="item"
              class="px-3 py-1.5 bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 rounded-lg text-sm font-medium hover:bg-brand-100 dark:hover:bg-brand-900/30 hover:text-brand-700 dark:hover:text-brand-400 transition-colors duration-200"
            >
              {{ item }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Code, Server, Brain, Database, Layout, Boxes } from 'lucide-vue-next'
import { techStack } from '../data/mock'

const categories = [
  {
    title: 'Languages',
    icon: Code,
    items: techStack.languages
  },
  {
    title: 'Backend',
    icon: Server,
    items: techStack.backend
  },
  {
    title: 'AI & Voice',
    icon: Brain,
    items: techStack.aiVoice
  },
  {
    title: 'Databases & Infrastructure',
    icon: Database,
    items: techStack.databases
  },
  {
    title: 'Frontend',
    icon: Layout,
    items: techStack.frontend
  },
  {
    title: 'Architecture',
    icon: Boxes,
    items: techStack.architecture
  }
]
</script>
