<template>
  <div class="pt-20">
    <div class="max-w-4xl mx-auto px-6 py-20">
      <template v-if="project">
        <!-- Back Button -->
        <router-link to="/projects" class="inline-flex items-center gap-2 text-zinc-600 dark:text-zinc-400 hover:text-brand-500 dark:hover:text-brand-400 mb-8 transition-colors duration-200 animate-fade-in">
          <ArrowLeft class="w-4 h-4" />
          Back to Projects
        </router-link>

        <!-- Header -->
        <div class="mb-12 animate-fade-in">
          <p class="text-brand-500 dark:text-brand-400 font-medium mb-2">{{ project.subtitle }}</p>
          <h1 class="text-3xl md:text-4xl font-bold text-zinc-900 dark:text-white mb-4">{{ project.title }}</h1>
          <p class="text-lg text-zinc-600 dark:text-zinc-400">{{ project.overview }}</p>
          <div class="w-20 h-1 bg-brand-500 rounded-full mt-6"></div>
        </div>

        <!-- Tech Stack -->
        <div class="mb-12 animate-slide-up">
          <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-4 flex items-center gap-3">
            <Layers class="w-5 h-5 text-brand-500" />
            Tech Stack
          </h2>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="tech in project.techStack"
              :key="tech"
              class="px-3 py-1.5 bg-brand-100 dark:bg-brand-900/30 text-brand-700 dark:text-brand-400 rounded-lg text-sm font-medium"
            >
              {{ tech }}
            </span>
          </div>
        </div>

        <!-- Problem -->
        <div class="mb-12 animate-slide-up" style="animation-delay: 0.1s">
          <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-4 flex items-center gap-3">
            <AlertCircle class="w-5 h-5 text-brand-500" />
            Problem Statement
          </h2>
          <p class="text-zinc-600 dark:text-zinc-400 leading-relaxed">{{ project.problem }}</p>
        </div>

        <!-- Solution -->
        <div class="mb-12 animate-slide-up" style="animation-delay: 0.15s">
          <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-4 flex items-center gap-3">
            <Lightbulb class="w-5 h-5 text-brand-500" />
            Solution
          </h2>
          <p class="text-zinc-600 dark:text-zinc-400 leading-relaxed">{{ project.solution }}</p>
        </div>

        <!-- Engineering Challenges -->
        <div class="mb-12 animate-slide-up" style="animation-delay: 0.2s">
          <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-4 flex items-center gap-3">
            <Wrench class="w-5 h-5 text-brand-500" />
            Engineering Challenges
          </h2>
          <ul class="space-y-3">
            <li
              v-for="(challenge, index) in project.challenges"
              :key="index"
              class="flex items-start gap-3 text-zinc-600 dark:text-zinc-400"
            >
              <ChevronRight class="w-5 h-5 text-brand-500 flex-shrink-0 mt-0.5" />
              <span>{{ challenge }}</span>
            </li>
          </ul>
        </div>

        <!-- Architecture -->
        <div class="animate-slide-up" style="animation-delay: 0.25s">
          <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-4 flex items-center gap-3">
            <Server class="w-5 h-5 text-brand-500" />
            Key Architectural Decisions
          </h2>
          <ul class="space-y-3">
            <li
              v-for="(decision, index) in project.architecture"
              :key="index"
              class="flex items-start gap-3 text-zinc-600 dark:text-zinc-400"
            >
              <ChevronRight class="w-5 h-5 text-brand-500 flex-shrink-0 mt-0.5" />
              <span>{{ decision }}</span>
            </li>
          </ul>
        </div>
      </template>

      <!-- Not Found -->
      <template v-else>
        <div class="text-center py-20">
          <h1 class="text-2xl font-bold text-zinc-900 dark:text-white mb-4">Project not found</h1>
          <router-link to="/projects">
            <Button variant="primary">View all projects</Button>
          </router-link>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { ArrowLeft, Layers, AlertCircle, Lightbulb, Wrench, Server, ChevronRight } from 'lucide-vue-next'
import Button from '../components/Button.vue'
import { projects } from '../data/mock'

const route = useRoute()

const project = computed(() => {
  return projects.find(p => p.slug === route.params.slug)
})
</script>
