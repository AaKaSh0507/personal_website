<template>
  <div class="pt-20">
    <div class="max-w-4xl mx-auto px-6 py-20">
      <!-- Header -->
      <div class="mb-12 animate-fade-in">
        <h1 class="text-3xl md:text-4xl font-bold text-zinc-900 dark:text-white mb-4">Get in Touch</h1>
        <p class="text-lg text-zinc-600 dark:text-zinc-400">Have a project in mind or want to discuss opportunities? I'd love to hear from you.</p>
        <div class="w-20 h-1 bg-brand-500 rounded-full mt-4"></div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Contact Info -->
        <div class="animate-slide-up">
          <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-6">Contact Information</h2>
          
          <div class="space-y-4">
            <a
              :href="`mailto:${socialLinks.email}`"
              class="flex items-center gap-4 p-4 bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl hover:border-brand-300 dark:hover:border-brand-700 transition-colors duration-300 group"
            >
              <div class="p-3 rounded-lg bg-brand-100 dark:bg-brand-900/30 group-hover:bg-brand-200 dark:group-hover:bg-brand-900/50 transition-colors duration-200">
                <Mail class="w-5 h-5 text-brand-600 dark:text-brand-400" />
              </div>
              <div>
                <p class="text-sm text-zinc-500 dark:text-zinc-500">Email</p>
                <p class="text-zinc-900 dark:text-white font-medium">{{ socialLinks.email }}</p>
              </div>
            </a>

            <a
              :href="socialLinks.linkedin"
              target="_blank"
              rel="noopener noreferrer"
              class="flex items-center gap-4 p-4 bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl hover:border-brand-300 dark:hover:border-brand-700 transition-colors duration-300 group"
            >
              <div class="p-3 rounded-lg bg-brand-100 dark:bg-brand-900/30 group-hover:bg-brand-200 dark:group-hover:bg-brand-900/50 transition-colors duration-200">
                <Linkedin class="w-5 h-5 text-brand-600 dark:text-brand-400" />
              </div>
              <div>
                <p class="text-sm text-zinc-500 dark:text-zinc-500">LinkedIn</p>
                <p class="text-zinc-900 dark:text-white font-medium">linkedin.com/in/aakash-malik05</p>
              </div>
            </a>

            <a
              :href="socialLinks.github"
              target="_blank"
              rel="noopener noreferrer"
              class="flex items-center gap-4 p-4 bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl hover:border-brand-300 dark:hover:border-brand-700 transition-colors duration-300 group"
            >
              <div class="p-3 rounded-lg bg-brand-100 dark:bg-brand-900/30 group-hover:bg-brand-200 dark:group-hover:bg-brand-900/50 transition-colors duration-200">
                <Github class="w-5 h-5 text-brand-600 dark:text-brand-400" />
              </div>
              <div>
                <p class="text-sm text-zinc-500 dark:text-zinc-500">GitHub</p>
                <p class="text-zinc-900 dark:text-white font-medium">github.com/AaKaSh0507</p>
              </div>
            </a>
          </div>
        </div>

        <!-- Contact Form -->
        <div class="animate-slide-up" style="animation-delay: 0.1s">
          <h2 class="text-xl font-semibold text-zinc-900 dark:text-white mb-6">Send a Message</h2>
          
          <form @submit.prevent="submitForm" class="space-y-6">
            <div>
              <label for="name" class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Name</label>
              <input
                v-model="form.name"
                type="text"
                id="name"
                required
                class="w-full px-4 py-3 bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl text-zinc-900 dark:text-white placeholder-zinc-400 dark:placeholder-zinc-600 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-transparent transition-all duration-200"
                placeholder="Your name"
              />
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Email</label>
              <input
                v-model="form.email"
                type="email"
                id="email"
                required
                class="w-full px-4 py-3 bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl text-zinc-900 dark:text-white placeholder-zinc-400 dark:placeholder-zinc-600 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-transparent transition-all duration-200"
                placeholder="your@email.com"
              />
            </div>

            <div>
              <label for="message" class="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">Message</label>
              <textarea
                v-model="form.message"
                id="message"
                required
                rows="5"
                class="w-full px-4 py-3 bg-light-card dark:bg-dark-card border border-light-border dark:border-dark-border rounded-xl text-zinc-900 dark:text-white placeholder-zinc-400 dark:placeholder-zinc-600 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-transparent transition-all duration-200 resize-none"
                placeholder="Your message..."
              ></textarea>
            </div>

            <Button type="submit" variant="primary" size="lg" fullWidth :loading="isSubmitting">
              <Send class="w-5 h-5" />
              Send Message
            </Button>

            <p v-if="submitStatus === 'success'" class="text-green-600 dark:text-green-400 text-sm text-center">
              Message sent successfully! I'll get back to you soon.
            </p>
            <p v-if="submitStatus === 'error'" class="text-red-600 dark:text-red-400 text-sm text-center">
              Failed to send message. Please try again or email directly.
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { Mail, Linkedin, Github, Send } from 'lucide-vue-next'
import Button from '../components/Button.vue'
import { socialLinks } from '../data/mock'

const form = reactive({
  name: '',
  email: '',
  message: ''
})

const isSubmitting = ref(false)
const submitStatus = ref(null)

const submitForm = async () => {
  isSubmitting.value = true
  submitStatus.value = null
  
  // Simulate form submission (mock)
  // In production, this would send to a backend API
  try {
    await new Promise(resolve => setTimeout(resolve, 1500))
    
    // Store in localStorage for demo purposes
    const messages = JSON.parse(localStorage.getItem('contactMessages') || '[]')
    messages.push({
      ...form,
      timestamp: new Date().toISOString()
    })
    localStorage.setItem('contactMessages', JSON.stringify(messages))
    
    submitStatus.value = 'success'
    form.name = ''
    form.email = ''
    form.message = ''
  } catch (error) {
    submitStatus.value = 'error'
  } finally {
    isSubmitting.value = false
  }
}
</script>
