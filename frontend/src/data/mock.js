// Mock data for Aakash Malik's portfolio

export const profile = {
  name: 'Aakash Malik',
  title: 'Software Development Engineer | Backend & Full-stack Systems',
  tagline: 'Building scalable systems with and without AI.',
  intro: `I am a software engineer with a strong focus on backend and system design, experienced in building scalable, production-grade applications across startups and product teams. My work spans distributed backend systems, multi-tenant platforms, and AI-enabled products, with an emphasis on clean architecture, performance, and reliability.`,
  snapshot: `I have worked on real-world systems ranging from enterprise RBAC platforms and AI voice agents to multi-tenant exam preparation platforms. I enjoy working close to core infrastructure, solving hard backend problems, and designing systems that scale cleanly as usage grows.`,
  email: 'aakash.malik@example.com',
  linkedin: 'https://linkedin.com/in/aakashmalik',
  github: 'https://github.com/aakashmalik',
  profileImage: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face'
}

export const aboutContent = {
  bio: `I am a software engineer with a strong interest in backend systems, distributed architectures, and building reliable software that scales with real-world usage. I recently completed my B.Tech in Computer Science and Engineering and pursued advanced training in Machine Learning and Data Science to strengthen my understanding of modern AI-driven systems.

My experience spans internships and independent projects where I worked on production systems used by hundreds to thousands of users. I have designed backend services, authorization systems, and data models, and I am comfortable working across the stack when needed. I value clarity in system design, thoughtful trade-offs, and writing code that remains maintainable over time.

While I have worked on AI-heavy systems such as agentic platforms and voice-based automation, I view AI as a tool rather than a goal. My primary focus remains building solid engineering foundations, whether the system uses AI or not.`,
  interests: ['Reading', 'Writing short shayaris', 'Playing cricket and badminton', 'Bike rides', 'Maintaining a regular fitness routine']
}

export const experiences = [
  {
    id: 1,
    title: 'SDE Intern',
    company: 'DPDzero Technologies',
    location: 'Bangalore',
    period: 'May 2025 – September 2025',
    highlights: [
      'Built backend services for AI voice agent infrastructure',
      'Designed enterprise-grade multi-tenant RBAC systems',
      'Worked on scalable microservices using FastAPI',
      'Contributed full-stack features using Vue.js and PostgreSQL',
      'Supported production deployments via containerized services'
    ]
  },
  {
    id: 2,
    title: 'Web Developer Intern',
    company: 'ImageKit.io',
    location: 'Remote',
    period: 'January 2024 – May 2024',
    highlights: [
      'Built full-stack web applications with Vue.js',
      'Implemented REST APIs using Django REST Framework',
      'Integrated CDN-based image delivery',
      'Worked in a remote, production-oriented environment'
    ]
  }
]

export const projects = [
  {
    id: 1,
    slug: 'saadhaka',
    title: 'Saadhaka',
    subtitle: 'Agentic AI Platform',
    overview: 'Enterprise agentic AI platform for orchestrating distributed AI agents.',
    techStack: ['FastAPI', 'LangChain', 'Hugging Face', 'Docker', 'Redis', 'PostgreSQL'],
    problem: 'Organizations struggle to coordinate multiple AI agents working on complex, multi-step tasks. Traditional approaches lack proper orchestration, state management, and enterprise-grade reliability.',
    solution: 'Built a comprehensive platform that enables seamless orchestration of distributed AI agents with built-in state management, fault tolerance, and enterprise security features.',
    challenges: [
      'Designing a reliable message-passing system for inter-agent communication',
      'Implementing proper state persistence across distributed agent workflows',
      'Building enterprise-grade authentication and multi-tenancy support',
      'Optimizing response latency while maintaining conversation context'
    ],
    architecture: [
      'Microservices architecture with FastAPI for high-performance APIs',
      'Redis-based message queue for async agent communication',
      'PostgreSQL for persistent state and audit logging',
      'Docker containerization for scalable deployments'
    ]
  },
  {
    id: 2,
    slug: 'schedula',
    title: 'Schedula',
    subtitle: 'AI Voice Events Scheduler',
    overview: 'AI-powered voice system automating appointment scheduling via phone calls.',
    techStack: ['Twilio', 'LiveKit', 'GPT-based models', 'Flask', 'Webhooks'],
    problem: 'Manual appointment scheduling via phone is time-consuming and error-prone. Businesses need an automated solution that handles natural conversations and integrates with existing calendar systems.',
    solution: 'Developed an AI voice assistant that conducts natural phone conversations, understands scheduling intents, and automatically books appointments while handling edge cases gracefully.',
    challenges: [
      'Achieving low-latency voice processing for natural conversations',
      'Handling interruptions and context switches mid-conversation',
      'Integrating with various calendar and CRM systems',
      'Managing voice quality across different network conditions'
    ],
    architecture: [
      'Twilio for telephony infrastructure and call handling',
      'LiveKit for real-time voice processing',
      'GPT models for natural language understanding',
      'Webhook-based integration with external systems'
    ]
  },
  {
    id: 3,
    slug: 'vichintarka',
    title: 'Vichintarka',
    subtitle: 'Multi-tenant Exam Platform',
    overview: 'Scalable exam preparation platform for competitive exams.',
    techStack: ['FastAPI', 'PostgreSQL', 'Vue.js', 'Redis', 'S3-compatible storage'],
    problem: 'Exam preparation platforms often struggle with scalability during peak usage and lack proper isolation between different coaching institutes or user groups.',
    solution: 'Built a multi-tenant architecture that provides complete data isolation, customizable branding per tenant, and handles traffic spikes during exam seasons.',
    challenges: [
      'Implementing proper tenant isolation at the database level',
      'Designing a flexible question bank with various question types',
      'Building real-time test-taking with anti-cheating measures',
      'Scaling to handle thousands of concurrent test-takers'
    ],
    architecture: [
      'FastAPI with async endpoints for high concurrency',
      'PostgreSQL with row-level security for tenant isolation',
      'Redis for session management and caching',
      'S3-compatible storage for media assets'
    ]
  }
]

export const techStack = {
  languages: ['Python', 'JavaScript', 'SQL'],
  backend: ['FastAPI', 'Django', 'Flask'],
  aiVoice: ['LangChain', 'Hugging Face', 'OpenAI APIs', 'Deepgram', 'ElevenLabs', 'LiveKit', 'Twilio'],
  databases: ['PostgreSQL', 'MongoDB', 'Redis', 'Docker', 'CI/CD'],
  frontend: ['Vue.js', 'Tailwind CSS', 'Vuetify'],
  architecture: ['Microservices', 'Multi-tenant systems', 'RBAC', 'REST APIs']
}

export const socialLinks = {
  email: 'aakash.malik@example.com',
  linkedin: 'https://linkedin.com/in/aakashmalik',
  github: 'https://github.com/aakashmalik'
}
