<template>
  <div class="pt-20">
    <div class="max-w-6xl mx-auto px-6 py-20">
      <!-- Header -->
      <div class="mb-12 animate-fade-in">
        <h1 class="text-3xl md:text-4xl font-bold text-zinc-900 dark:text-white mb-4">Projects</h1>
        <p class="text-lg text-zinc-600 dark:text-zinc-400">Production-grade systems I've designed and built</p>
        <div class="w-20 h-1 bg-brand-500 rounded-full mt-4"></div>
      </div>

      <!-- Projects Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 animate-slide-up">
        <ProjectCard v-for="project in projects" :key="project.id" :project="project" />
      </div>
    </div>
  </div>
</template>

<script setup>
import ProjectCard from '../components/ProjectCard.vue'
import { projects } from '../data/mock'
</script>
