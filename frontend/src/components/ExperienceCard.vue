<template>
  <div class="relative pl-8 pb-12 last:pb-0">
    <!-- Timeline line -->
    <div class="absolute left-[11px] top-2 bottom-0 w-px bg-light-border dark:bg-dark-border last:hidden"></div>
    
    <!-- Timeline dot -->
    <div class="absolute left-0 top-2 w-6 h-6 rounded-full bg-brand-100 dark:bg-brand-900/30 border-2 border-brand-500 flex items-center justify-center">
      <div class="w-2 h-2 rounded-full bg-brand-500"></div>
    </div>

    <!-- Content -->
    <div class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-6">
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 mb-4">
        <div>
          <h3 class="text-lg font-semibold text-zinc-900 dark:text-white">{{ experience.title }}</h3>
          <p class="text-brand-500 dark:text-brand-400 font-medium">{{ experience.company }}</p>
        </div>
        <div class="flex flex-col sm:items-end">
          <span class="text-sm text-zinc-600 dark:text-zinc-400">{{ experience.period }}</span>
          <span class="text-sm text-zinc-500 dark:text-zinc-500">{{ experience.location }}</span>
        </div>
      </div>

      <ul class="space-y-2">
        <li
          v-for="(highlight, index) in experience.highlights"
          :key="index"
          class="flex items-start gap-3 text-sm text-zinc-600 dark:text-zinc-400"
        >
          <ChevronRight class="w-4 h-4 text-brand-500 flex-shrink-0 mt-0.5" />
          <span>{{ highlight }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ChevronRight } from 'lucide-vue-next'

defineProps({
  experience: {
    type: Object,
    required: true
  }
})
</script>
