// Data for Aakash Malik's portfolio - extracted from resume

export const profile = {
  name: 'Aakash Malik',
  title: 'Software Development Engineer | Backend & Full-stack Systems',
  tagline: 'Building scalable systems with and without AI.',
  intro: `I am a software engineer with a strong focus on backend and system design, experienced in building scalable, production-grade applications across startups and product teams. My work spans distributed backend systems, multi-tenant platforms, and AI-enabled products, with an emphasis on clean architecture, performance, and reliability.`,
  snapshot: `I have worked on real-world systems ranging from enterprise RBAC platforms and AI voice agents to multi-tenant exam preparation platforms. I enjoy working close to core infrastructure, solving hard backend problems, and designing systems that scale cleanly as usage grows.`,
  email: 'work.aakashm@gmail.com',
  phone: '+91-8273972303',
  linkedin: 'https://www.linkedin.com/in/aakash-malik05',
  github: 'https://www.github.com/AaKaSh0507',
  location: 'Bangalore, India',
  profileImage: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face',
  resumeUrl: 'https://customer-assets.emergentagent.com/job_aakash-engineer/artifacts/0dfk2u8o_Aakash_Malik_SDE_Resume.pdf'
}

export const aboutContent = {
  bio: `I am a software engineer with a strong interest in backend systems, distributed architectures, and building reliable software that scales with real-world usage. I recently completed my B.Tech in Computer Science and Engineering from Shiv Nadar Institution of Eminence and pursued a PG Diploma in Machine Learning and Data Science from IIT Roorkee to strengthen my understanding of modern AI-driven systems.

My experience spans internships and independent projects where I worked on production systems used by hundreds to thousands of users. I have designed backend services, authorization systems, and data models, and I am comfortable working across the stack when needed. I value clarity in system design, thoughtful trade-offs, and writing code that remains maintainable over time.

While I have worked on AI-heavy systems such as agentic platforms and voice-based automation, I view AI as a tool rather than a goal. My primary focus remains building solid engineering foundations, whether the system uses AI or not.`,
  interests: ['Reading', 'Writing short shayaris', 'Playing cricket and badminton', 'Bike rides', 'Maintaining a regular fitness routine']
}

export const education = [
  {
    id: 1,
    institution: 'IIT Roorkee',
    degree: 'PG Diploma in Machine Learning and Data Science',
    period: "May'24 - Apr'25",
    description: 'Advanced training in Machine Learning, Deep Learning, and Data Science methodologies.'
  },
  {
    id: 2,
    institution: 'Shiv Nadar Institution of Eminence',
    degree: 'B.Tech in Computer Science and Engineering',
    period: "Aug'20 - Aug'24",
    description: 'Comprehensive education in computer science fundamentals, algorithms, and software engineering.'
  }
]

export const experiences = [
  {
    id: 1,
    title: 'SDE Intern',
    company: 'DPDzero Technologies',
    location: 'Bangalore',
    period: "May'25 - Sep'25",
    highlights: [
      'Architected AI voice agent infrastructure for collections automation with LiveKit orchestration and SIP routing',
      'Built Saadhaka - an enterprise agentic AI platform using FastAPI microservices, LangChain, and Hugging Face Transformers',
      'Engineered enterprise multi-tenant RBAC platform serving 1000+ users with sub-100ms authorization checks at 200 QPS',
      'Implemented Redis-backed caching reducing database load by 60%',
      'Delivered full-stack solution with FastAPI backend, PostgreSQL, Vue.js frontend (Vuetify/Tailwind), and CI/CD pipelines for horizontal scaling'
    ]
  },
  {
    id: 2,
    title: 'Web Developer Intern',
    company: 'ImageKit.io',
    location: 'Remote',
    period: "Jan'24 - May'24",
    highlights: [
      'Built full-stack e-commerce platform with Vue.js frontend and ImageKit.io CDN integration, improving page load performance',
      'Implemented scalable RESTful API architecture using Django REST Framework with JWT authentication',
      'Designed and maintained PostgreSQL database schemas for optimal performance',
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
    overview: 'Enterprise agentic AI platform for orchestrating distributed AI agents with 99.5% uptime.',
    techStack: ['FastAPI', 'LangChain', 'Hugging Face', 'Docker', 'SQLAlchemy ORM', 'OpenAI API', 'Redis', 'CI/CD'],
    problem: 'Organizations struggle to coordinate multiple AI agents working on complex, multi-step tasks. Traditional approaches lack proper orchestration, state management, and enterprise-grade reliability.',
    solution: 'Built an enterprise agentic AI platform with FastAPI microservices, Docker containerization, and SQLAlchemy ORM, implementing a plugin architecture for distributed AI agent orchestration.',
    challenges: [
      'Designing a reliable message-passing system for inter-agent communication',
      'Implementing proper state persistence across distributed agent workflows',
      'Building enterprise-grade authentication and multi-tenancy support',
      'Optimizing LLM inference latency by 40% using Redis caching at 100+ RPS'
    ],
    architecture: [
      'FastAPI microservices with plugin architecture for distributed AI agent orchestration',
      'Docker containerization for scalable deployments',
      'Integrated Hugging Face Transformers, LangChain, and OpenAI API',
      'CI/CD pipelines achieving 99.5% uptime',
      'Redis caching reducing LLM inference latency by 40%'
    ]
  },
  {
    id: 2,
    slug: 'schedula',
    title: 'Schedula',
    subtitle: 'AI Voice Events Scheduler',
    overview: 'End-to-end AI voice agent for pharmaceutical appointment scheduling via phone calls.',
    techStack: ['Twilio', 'LiveKit', 'GPT-4o', 'Deepgram STT', 'ElevenLabs TTS', 'Flask', 'Brevo'],
    problem: 'Manual appointment scheduling via phone is time-consuming and error-prone. Pharmaceutical businesses need an automated solution that handles natural conversations and integrates with calendar and email systems.',
    solution: 'Engineered an end-to-end AI voice agent integrating Twilio telephony with LiveKit streaming and a multi-service AI pipeline (Deepgram STT, GPT-4o, ElevenLabs TTS).',
    challenges: [
      'Achieving low-latency voice processing for natural conversations',
      'Integrating multiple AI services (STT, LLM, TTS) in real-time pipeline',
      'Managing complete call lifecycle with validation and error handling',
      'Building responsive dashboard for tracking concurrent calls'
    ],
    architecture: [
      'Twilio for telephony infrastructure with LiveKit streaming integration',
      'Multi-service AI pipeline: Deepgram STT → GPT-4o → ElevenLabs TTS',
      'Flask webhook architecture managing complete call lifecycle',
      'Automated appointment creation with JSON persistence',
      'Brevo email confirmations and responsive dashboard'
    ]
  },
  {
    id: 3,
    slug: 'vichintarka',
    title: 'Vichintarka',
    subtitle: 'Multi-tenant Exam Platform',
    overview: 'Scalable multi-tenant exam preparation platform for JEE/NEET competitive exams.',
    techStack: ['FastAPI', 'PostgreSQL', 'Vue.js', 'SQLAlchemy ORM', 'Redis', 'LaTeX', 'ReportLab', 'S3'],
    problem: 'Exam preparation platforms often struggle with scalability during peak usage and lack proper isolation between different coaching institutes or user groups.',
    solution: 'Architected a scalable multi-tenant exam platform implementing microservices architecture with FastAPI, SQLAlchemy ORM, and organization-scoped data isolation serving multiple competitive exam categories.',
    challenges: [
      'Implementing proper tenant isolation at the database level with organization-scoped data',
      'Designing comprehensive testing infrastructure with LaTeX rendering for mathematical questions',
      'Building browser-based anti-cheat enforcement (fullscreen/tab-switch detection)',
      'Scaling to handle thousands of concurrent test-takers during exam seasons'
    ],
    architecture: [
      'FastAPI with SQLAlchemy ORM for high-performance APIs',
      'PostgreSQL with organization-scoped data isolation for multi-tenancy',
      'Redis-backed caching for session management and performance',
      'LaTeX rendering for mathematical content',
      'PDF generation with ReportLab and S3 storage for results',
      'Analytics engine tracking per-question accuracy and weak area detection'
    ]
  }
]

export const techStack = {
  languages: ['Python', 'JavaScript (ES6+)', 'SQL'],
  backend: ['FastAPI', 'Django', 'Flask', 'SQLAlchemy'],
  aiVoice: ['LangChain', 'Hugging Face', 'OpenAI API', 'Deepgram STT', 'ElevenLabs TTS', 'LiveKit', 'Twilio'],
  databases: ['PostgreSQL', 'MongoDB', 'Redis', 'Docker', 'Git', 'CI/CD'],
  frontend: ['Vue.js', 'Vuetify', 'Tailwind CSS', 'HTML5', 'CSS3'],
  architecture: ['Microservices', 'Multi-tenant RBAC', 'RESTful APIs', 'WebRTC', 'Distributed Caching', 'Horizontal Scaling']
}

export const socialLinks = {
  email: 'work.aakashm@gmail.com',
  linkedin: 'https://www.linkedin.com/in/aakash-malik05',
  github: 'https://www.github.com/AaKaSh0507'
}
