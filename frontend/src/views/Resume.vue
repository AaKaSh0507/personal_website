<template>
  <div class="pt-20">
    <div class="max-w-4xl mx-auto px-6 py-20">
      <!-- Header -->
      <div class="mb-12 animate-fade-in">
        <h1 class="text-3xl md:text-4xl font-bold text-zinc-900 dark:text-white mb-4">Resume</h1>
        <p class="text-lg text-zinc-600 dark:text-zinc-400">Download my resume or view highlights below</p>
        <div class="w-20 h-1 bg-brand-500 rounded-full mt-4"></div>
      </div>

      <!-- Download Button -->
      <div class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-8 mb-12 animate-slide-up">
        <div class="flex flex-col sm:flex-row items-center justify-between gap-6">
          <div class="flex items-center gap-4">
            <div class="p-3 rounded-xl bg-brand-100 dark:bg-brand-900/30">
              <FileText class="w-8 h-8 text-brand-600 dark:text-brand-400" />
            </div>
            <div>
              <h2 class="text-lg font-semibold text-zinc-900 dark:text-white">Aakash_Malik_Resume.pdf</h2>
              <p class="text-sm text-zinc-500 dark:text-zinc-500">Last updated: July 2025</p>
            </div>
          </div>
          <a href="#" @click.prevent="downloadResume" class="w-full sm:w-auto">
            <Button variant="primary" size="lg" fullWidth class="sm:w-auto">
              <Download class="w-5 h-5" />
              Download Resume
            </Button>
          </a>
        </div>
      </div>

      <!-- Resume Highlights -->
      <div class="space-y-8 animate-slide-up" style="animation-delay: 0.1s">
        <!-- Summary -->
        <div class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-6">
          <h3 class="text-lg font-semibold text-zinc-900 dark:text-white mb-4 flex items-center gap-3">
            <User class="w-5 h-5 text-brand-500" />
            Summary
          </h3>
          <p class="text-zinc-600 dark:text-zinc-400 leading-relaxed">
            Software Development Engineer with focus on backend systems, distributed architectures, and scalable application design. Experienced in building production-grade systems across startups, with expertise in FastAPI, Python, PostgreSQL, and AI-enabled platforms.
          </p>
        </div>

        <!-- Skills -->
        <div class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-6">
          <h3 class="text-lg font-semibold text-zinc-900 dark:text-white mb-4 flex items-center gap-3">
            <Code class="w-5 h-5 text-brand-500" />
            Key Skills
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <p class="text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Backend & Systems</p>
              <p class="text-sm text-zinc-600 dark:text-zinc-400">FastAPI, Django, Flask, PostgreSQL, MongoDB, Redis, Docker</p>
            </div>
            <div>
              <p class="text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">AI & Voice</p>
              <p class="text-sm text-zinc-600 dark:text-zinc-400">LangChain, Hugging Face, OpenAI APIs, Twilio, LiveKit</p>
            </div>
            <div>
              <p class="text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Frontend</p>
              <p class="text-sm text-zinc-600 dark:text-zinc-400">Vue.js, Tailwind CSS, Vuetify</p>
            </div>
            <div>
              <p class="text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Architecture</p>
              <p class="text-sm text-zinc-600 dark:text-zinc-400">Microservices, Multi-tenant systems, RBAC, REST APIs</p>
            </div>
          </div>
        </div>

        <!-- Experience Preview -->
        <div class="bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl p-6">
          <h3 class="text-lg font-semibold text-zinc-900 dark:text-white mb-4 flex items-center gap-3">
            <Briefcase class="w-5 h-5 text-brand-500" />
            Experience
          </h3>
          <div class="space-y-4">
            <div class="flex items-start justify-between">
              <div>
                <p class="font-medium text-zinc-900 dark:text-white">SDE Intern</p>
                <p class="text-sm text-brand-500 dark:text-brand-400">DPDzero Technologies, Bangalore</p>
              </div>
              <p class="text-sm text-zinc-500">May 2025 – Sep 2025</p>
            </div>
            <div class="flex items-start justify-between">
              <div>
                <p class="font-medium text-zinc-900 dark:text-white">Web Developer Intern</p>
                <p class="text-sm text-brand-500 dark:text-brand-400">ImageKit.io (Remote)</p>
              </div>
              <p class="text-sm text-zinc-500">Jan 2024 – May 2024</p>
            </div>
          </div>
          <router-link to="/experience" class="inline-flex items-center gap-2 text-brand-500 hover:text-brand-600 text-sm font-medium mt-4 transition-colors duration-200">
            View full experience
            <ArrowRight class="w-4 h-4" />
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { FileText, Download, User, Code, Briefcase, ArrowRight } from 'lucide-vue-next'
import Button from '../components/Button.vue'

const downloadResume = () => {
  // In production, this would download an actual PDF
  alert('Resume download will be available once the PDF is uploaded. Please contact via the Contact page for now.')
}
</script>
