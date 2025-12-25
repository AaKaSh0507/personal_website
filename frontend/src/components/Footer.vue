<template>
  <footer class="border-t border-light-border dark:border-dark-border bg-light-bg dark:bg-dark-bg">
    <div class="max-w-6xl mx-auto px-6 py-12">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Brand -->
        <div>
          <h3 class="text-lg font-bold text-zinc-900 dark:text-white mb-2">Aakash Malik</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-400">Software Development Engineer</p>
          <p class="text-sm text-zinc-500 dark:text-zinc-500 mt-1">Building scalable systems with and without AI.</p>
        </div>

        <!-- Quick Links -->
        <div>
          <h4 class="text-sm font-semibold text-zinc-900 dark:text-white mb-4">Quick Links</h4>
          <div class="flex flex-col gap-2">
            <router-link
              v-for="link in quickLinks"
              :key="link.path"
              :to="link.path"
              class="text-sm text-zinc-600 dark:text-zinc-400 hover:text-brand-500 dark:hover:text-brand-400 transition-colors duration-200"
            >
              {{ link.name }}
            </router-link>
          </div>
        </div>

        <!-- Connect -->
        <div>
          <h4 class="text-sm font-semibold text-zinc-900 dark:text-white mb-4">Connect</h4>
          <div class="flex gap-4">
            <a
              :href="socialLinks.github"
              target="_blank"
              rel="noopener noreferrer"
              class="p-2 rounded-lg text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-white hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-all duration-200"
              aria-label="GitHub"
            >
              <Github class="w-5 h-5" />
            </a>
            <a
              :href="socialLinks.linkedin"
              target="_blank"
              rel="noopener noreferrer"
              class="p-2 rounded-lg text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-white hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-all duration-200"
              aria-label="LinkedIn"
            >
              <Linkedin class="w-5 h-5" />
            </a>
            <a
              :href="`mailto:${socialLinks.email}`"
              class="p-2 rounded-lg text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-white hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-all duration-200"
              aria-label="Email"
            >
              <Mail class="w-5 h-5" />
            </a>
          </div>
        </div>
      </div>

      <!-- Copyright -->
      <div class="mt-8 pt-8 border-t border-light-border dark:border-dark-border">
        <p class="text-sm text-zinc-500 dark:text-zinc-500 text-center">
          © {{ currentYear }} Aakash Malik. All rights reserved.
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { Github, Linkedin, Mail } from 'lucide-vue-next'
import { socialLinks } from '../data/mock'

const currentYear = new Date().getFullYear()

const quickLinks = [
  { name: 'Projects', path: '/projects' },
  { name: 'Experience', path: '/experience' },
  { name: 'Resume', path: '/resume' },
  { name: 'Contact', path: '/contact' }
]
</script>
