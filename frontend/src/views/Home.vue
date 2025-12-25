<template>
  <div class="pt-20">
    <!-- Hero Section -->
    <section class="min-h-[85vh] flex items-center">
      <div class="max-w-6xl mx-auto px-6 py-20">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <!-- Content -->
          <div class="order-2 lg:order-1">
            <div class="animate-fade-in">
              <p class="text-brand-500 dark:text-brand-400 font-medium mb-4">Hello, I'm</p>
              <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-zinc-900 dark:text-white mb-4 leading-tight">
                {{ profile.name }}
              </h1>
              <p class="text-lg md:text-xl text-zinc-600 dark:text-zinc-400 mb-6">
                {{ profile.title }}
              </p>
              <p class="text-2xl md:text-3xl font-semibold text-zinc-800 dark:text-zinc-200 mb-8">
                {{ profile.tagline }}
              </p>
            </div>

            <div class="animate-slide-up" style="animation-delay: 0.1s">
              <p class="text-zinc-600 dark:text-zinc-400 mb-6 leading-relaxed">
                {{ profile.intro }}
              </p>
              <p class="text-zinc-600 dark:text-zinc-400 mb-8 leading-relaxed">
                {{ profile.snapshot }}
              </p>
            </div>

            <!-- CTAs -->
            <div class="flex flex-wrap gap-4 animate-slide-up" style="animation-delay: 0.2s">
              <router-link to="/projects">
                <Button variant="primary" size="lg">
                  <FolderOpen class="w-5 h-5" />
                  View Projects
                </Button>
              </router-link>
              <router-link to="/resume">
                <Button variant="outline" size="lg">
                  <Download class="w-5 h-5" />
                  Download Resume
                </Button>
              </router-link>
              <router-link to="/contact">
                <Button variant="secondary" size="lg">
                  <Mail class="w-5 h-5" />
                  Contact Me
                </Button>
              </router-link>
            </div>
          </div>

          <!-- Profile Image -->
          <div class="order-1 lg:order-2 flex justify-center lg:justify-end animate-fade-in">
            <div class="relative">
              <div class="w-64 h-64 md:w-80 md:h-80 rounded-2xl overflow-hidden border-4 border-light-border dark:border-dark-border shadow-2xl shadow-brand-500/10">
                <img
                  :src="profile.profileImage"
                  :alt="profile.name"
                  class="w-full h-full object-cover"
                />
              </div>
              <!-- Decorative elements -->
              <div class="absolute -z-10 -top-4 -right-4 w-64 h-64 md:w-80 md:h-80 rounded-2xl bg-brand-100 dark:bg-brand-900/20"></div>
              <div class="absolute -z-20 -top-8 -right-8 w-64 h-64 md:w-80 md:h-80 rounded-2xl bg-brand-50 dark:bg-brand-900/10"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Quick Stats -->
    <section class="py-16 bg-zinc-50 dark:bg-dark-card border-y border-light-border dark:border-dark-border">
      <div class="max-w-6xl mx-auto px-6">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div v-for="stat in stats" :key="stat.label" class="text-center">
            <p class="text-3xl md:text-4xl font-bold text-brand-500 dark:text-brand-400 mb-2">{{ stat.value }}</p>
            <p class="text-sm text-zinc-600 dark:text-zinc-400">{{ stat.label }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Projects Preview -->
    <section class="py-20">
      <div class="max-w-6xl mx-auto px-6">
        <div class="flex items-center justify-between mb-12">
          <div>
            <h2 class="text-2xl md:text-3xl font-bold text-zinc-900 dark:text-white mb-2">Featured Projects</h2>
            <p class="text-zinc-600 dark:text-zinc-400">Some of the systems I've built</p>
          </div>
          <router-link to="/projects" class="hidden md:flex items-center gap-2 text-brand-500 hover:text-brand-600 font-medium transition-colors duration-200">
            View all
            <ArrowRight class="w-4 h-4" />
          </router-link>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <ProjectCard v-for="project in projects" :key="project.id" :project="project" />
        </div>

        <div class="mt-8 text-center md:hidden">
          <router-link to="/projects">
            <Button variant="outline">
              View all projects
              <ArrowRight class="w-4 h-4" />
            </Button>
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { FolderOpen, Download, Mail, ArrowRight } from 'lucide-vue-next'
import Button from '../components/Button.vue'
import ProjectCard from '../components/ProjectCard.vue'
import { profile, projects } from '../data/mock'

const stats = [
  { value: '2+', label: 'Years Experience' },
  { value: '3+', label: 'Production Systems' },
  { value: '1000+', label: 'Users Served' },
  { value: '10+', label: 'Technologies' }
]
</script>
