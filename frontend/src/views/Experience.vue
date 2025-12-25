<template>
  <div class="pt-20">
    <div class="max-w-4xl mx-auto px-6 py-20">
      <!-- Header -->
      <div class="mb-12 animate-fade-in">
        <h1 class="text-3xl md:text-4xl font-bold text-zinc-900 dark:text-white mb-4">Experience</h1>
        <p class="text-lg text-zinc-600 dark:text-zinc-400">My professional journey in software development</p>
        <div class="w-20 h-1 bg-brand-500 rounded-full mt-4"></div>
      </div>

      <!-- Timeline -->
      <div class="animate-slide-up">
        <ExperienceCard
          v-for="exp in experiences"
          :key="exp.id"
          :experience="exp"
        />
      </div>

      <!-- Education -->
      <div class="mt-16 animate-slide-up" style="animation-delay: 0.1s">
        <h2 class="text-2xl font-bold text-zinc-900 dark:text-white mb-8 flex items-center gap-3">
          <GraduationCap class="w-6 h-6 text-brand-500" />
          Education
        </h2>
        
        <div class="space-y-6">
          <div v-for="edu in education" :key="edu.id" class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-6">
            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 mb-2">
              <div>
                <h3 class="text-lg font-semibold text-zinc-900 dark:text-white">{{ edu.degree }}</h3>
                <p class="text-brand-500 dark:text-brand-400 font-medium">{{ edu.institution }}</p>
              </div>
              <span class="text-sm text-zinc-500 dark:text-zinc-500">{{ edu.period }}</span>
            </div>
            <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-2">
              {{ edu.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { GraduationCap } from 'lucide-vue-next'
import ExperienceCard from '../components/ExperienceCard.vue'
import { experiences } from '../data/mock'
</script>
