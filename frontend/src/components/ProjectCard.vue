<template>
  <div
    class="group bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl overflow-hidden hover:border-brand-300 dark:hover:border-brand-700 transition-all duration-300 hover:shadow-lg hover:shadow-brand-500/5"
  >
    <router-link :to="`/projects/${project.slug}`" class="block p-6">
      <!-- Header -->
      <div class="flex items-start justify-between mb-4">
        <div>
          <h3 class="text-lg font-semibold text-zinc-900 dark:text-white group-hover:text-brand-500 dark:group-hover:text-brand-400 transition-colors duration-200">
            {{ project.title }}
          </h3>
          <p class="text-sm text-zinc-500 dark:text-zinc-500">{{ project.subtitle }}</p>
        </div>
        <ArrowUpRight class="w-5 h-5 text-zinc-400 group-hover:text-brand-500 dark:group-hover:text-brand-400 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-all duration-200" />
      </div>

      <!-- Overview -->
      <p class="text-sm text-zinc-600 dark:text-zinc-400 mb-4 line-clamp-2">
        {{ project.overview }}
      </p>

      <!-- Tech Stack -->
      <div class="flex flex-wrap gap-2">
        <span
          v-for="tech in project.techStack.slice(0, 4)"
          :key="tech"
          class="px-2 py-1 text-xs font-medium bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 rounded-md"
        >
          {{ tech }}
        </span>
        <span
          v-if="project.techStack.length > 4"
          class="px-2 py-1 text-xs font-medium bg-zinc-100 dark:bg-zinc-800 text-zinc-500 dark:text-zinc-500 rounded-md"
        >
          +{{ project.techStack.length - 4 }} more
        </span>
      </div>
    </router-link>
  </div>
</template>

<script setup>
import { ArrowUpRight } from 'lucide-vue-next'

defineProps({
  project: {
    type: Object,
    required: true
  }
})
</script>
