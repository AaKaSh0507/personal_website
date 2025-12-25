<template>
  <div class="pt-20">
    <div class="max-w-4xl mx-auto px-6 py-20">
      <!-- Header -->
      <div class="mb-12 animate-fade-in">
        <h1 class="text-3xl md:text-4xl font-bold text-zinc-900 dark:text-white mb-4">About Me</h1>
        <div class="w-20 h-1 bg-brand-500 rounded-full"></div>
      </div>

      <!-- Bio -->
      <div class="prose prose-zinc dark:prose-invert max-w-none mb-16 animate-slide-up">
        <div class="space-y-6">
          <p v-for="(paragraph, index) in bioParag" :key="index" class="text-lg text-zinc-600 dark:text-zinc-400 leading-relaxed">
            {{ paragraph }}
          </p>
        </div>
      </div>

      <!-- Personal Interests -->
      <div class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-8 animate-slide-up" style="animation-delay: 0.1s">
        <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-6 flex items-center gap-3">
          <Heart class="w-5 h-5 text-brand-500" />
          Personal Interests
        </h2>
        <div class="flex flex-wrap gap-3">
          <span
            v-for="interest in aboutContent.interests"
            :key="interest"
            class="px-4 py-2 bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 rounded-full text-sm font-medium hover:bg-brand-100 dark:hover:bg-brand-900/30 hover:text-brand-700 dark:hover:text-brand-400 transition-colors duration-200 cursor-default"
          >
            {{ interest }}
          </span>
        </div>
      </div>

      <!-- Values -->
      <div class="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6 animate-slide-up" style="animation-delay: 0.2s">
        <div v-for="value in values" :key="value.title" class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-6 hover:border-brand-300 dark:hover:border-brand-700 transition-colors duration-300">
          <component :is="value.icon" class="w-8 h-8 text-brand-500 mb-4" />
          <h3 class="text-lg font-semibold text-zinc-900 dark:text-white mb-2">{{ value.title }}</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400">{{ value.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Heart, Code, Zap, Users } from 'lucide-vue-next'
import { aboutContent } from '../data/mock'

const bioParag = aboutContent.bio.split('\n\n')

const values = [
  {
    icon: Code,
    title: 'Clean Architecture',
    description: 'I value clarity in system design and writing code that remains maintainable over time.'
  },
  {
    icon: Zap,
    title: 'Performance Focus',
    description: 'Building systems that scale cleanly as usage grows, with emphasis on reliability.'
  },
  {
    icon: Users,
    title: 'User-Centric',
    description: 'Creating production systems that serve real users effectively and efficiently.'
  }
]
</script>
