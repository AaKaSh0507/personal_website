<template>
  <div class="pt-20">
    <div class="max-w-4xl mx-auto px-6 py-20">
      <!-- Header -->
      <div class="mb-12 animate-fade-in">
        <h1 class="text-3xl md:text-4xl font-bold text-zinc-900 dark:text-white mb-4">Blog</h1>
        <p class="text-lg text-zinc-600 dark:text-zinc-400">Thoughts on engineering, systems, and technology</p>
        <div class="w-20 h-1 bg-brand-500 rounded-full mt-4"></div>
      </div>

      <!-- Coming Soon -->
      <div class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-12 text-center animate-slide-up">
        <div class="p-4 rounded-full bg-brand-100 dark:bg-brand-900/30 w-fit mx-auto mb-6">
          <PenLine class="w-8 h-8 text-brand-600 dark:text-brand-400" />
        </div>
        <h2 class="text-2xl font-semibold text-zinc-900 dark:text-white mb-4">Writing coming soon</h2>
        <p class="text-zinc-600 dark:text-zinc-400 max-w-md mx-auto">
          I'm working on articles about backend systems, architecture patterns, and lessons learned from building production systems. Stay tuned!
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { PenLine } from 'lucide-vue-next'
</script>
