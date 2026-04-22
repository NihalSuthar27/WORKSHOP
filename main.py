from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="PBS Construction - Building excellence with precision, innovation, and trust.">
    <title>PBS Construction | Building Excellence</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --primary: #f5a623;
            --primary-hover: #d48a14;
            --bg-color: #0a0a0a;
            --surface: #1a1a1a;
            --surface-light: #2a2a2a;
            --text-main: #f8f9fa;
            --text-muted: #adb5bd;
            --font-heading: 'Outfit', sans-serif;
            --font-body: 'Inter', sans-serif;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: var(--font-body);
            background-color: var(--bg-color);
            color: var(--text-main);
            line-height: 1.6;
            overflow-x: hidden;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: var(--font-heading);
            font-weight: 700;
            line-height: 1.2;
        }

        a {
            text-decoration: none;
            color: inherit;
        }

        ul {
            list-style: none;
        }

        /* Utility Classes */
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .section {
            padding: 6rem 0;
        }

        .section-header {
            text-align: center;
            margin-bottom: 4rem;
        }

        .section-subtitle {
            color: var(--primary);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-size: 0.9rem;
            display: block;
            margin-bottom: 0.5rem;
        }

        .section-title {
            font-size: 2.5rem;
            color: var(--text-main);
        }

        .btn {
            display: inline-block;
            padding: 1rem 2rem;
            font-weight: 600;
            border-radius: 4px;
            transition: var(--transition);
            cursor: pointer;
            border: none;
            font-family: var(--font-body);
        }

        .btn-primary {
            background-color: var(--primary);
            color: #000;
        }

        .btn-primary:hover {
            background-color: var(--primary-hover);
            transform: translateY(-2px);
        }

        .btn-outline {
            background: transparent;
            border: 2px solid var(--text-main);
            color: var(--text-main);
        }

        .btn-outline:hover {
            background: var(--text-main);
            color: #000;
            transform: translateY(-2px);
        }

        /* Navbar */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 1.5rem 0;
            z-index: 1000;
            transition: var(--transition);
            background: transparent;
        }

        .navbar.scrolled {
            background: rgba(10, 10, 10, 0.9);
            backdrop-filter: blur(10px);
            padding: 1rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-family: var(--font-heading);
            font-size: 2rem;
            font-weight: 800;
            color: var(--text-main);
            letter-spacing: 1px;
        }

        .logo span {
            color: var(--primary);
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            font-size: 0.95rem;
            font-weight: 500;
            transition: var(--transition);
            position: relative;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: -4px;
            left: 0;
            background-color: var(--primary);
            transition: var(--transition);
        }

        .nav-links a:hover::after,
        .nav-links a.active::after {
            width: 100%;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        /* Hamburger Menu */
        .menu-toggle {
            display: none;
            flex-direction: column;
            gap: 5px;
            cursor: pointer;
        }

        .menu-toggle span {
            width: 25px;
            height: 3px;
            background-color: var(--text-main);
            transition: var(--transition);
        }

        /* Hero Section */
        .hero {
            height: 100vh;
            display: flex;
            align-items: center;
            position: relative;
            background-color: #000B1A; /* Fallback matching Cognizance dark space blue */
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at center, transparent 0%, rgba(0,0,0,0.7) 100%);
            z-index: 0;
            pointer-events: none;
        }

        .hero-content {
            position: relative;
            z-index: 1;
            max-width: 800px;
        }

        .hero-title {
            font-size: 4.5rem;
            margin-bottom: 1.5rem;
            opacity: 0;
            transform: translateY(30px);
            animation: fadeUp 1s forwards 0.2s;
        }

        .hero-title span {
            color: var(--primary);
        }

        .hero-desc {
            font-size: 1.2rem;
            color: var(--text-muted);
            margin-bottom: 2.5rem;
            max-width: 600px;
            opacity: 0;
            transform: translateY(30px);
            animation: fadeUp 1s forwards 0.4s;
        }

        .hero-btns {
            display: flex;
            gap: 1rem;
            opacity: 0;
            transform: translateY(30px);
            animation: fadeUp 1s forwards 0.6s;
        }

        /* Services Section */
        .services {
            background-color: var(--bg-color);
            position: relative;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }

        .service-card {
            background-color: var(--surface);
            padding: 3rem 2rem;
            border-radius: 8px;
            transition: var(--transition);
            border: 1px solid rgba(255,255,255,0.05);
            position: relative;
            overflow: hidden;
        }

        .service-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background-color: var(--primary);
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.4s ease;
        }

        .service-card:hover {
            transform: translateY(-10px);
            background-color: var(--surface-light);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        .service-card:hover::before {
            transform: scaleX(1);
        }

        .service-icon {
            font-size: 3rem;
            color: var(--primary);
            margin-bottom: 1.5rem;
            display: inline-block;
        }

        .service-title {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .service-desc {
            color: var(--text-muted);
        }

        /* Projects Section */
        .projects {
            background-color: var(--surface);
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1.5rem;
        }

        .project-card {
            position: relative;
            border-radius: 8px;
            overflow: hidden;
            height: 300px;
            cursor: pointer;
        }

        .project-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s ease;
        }

        .project-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
            padding: 2rem;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            opacity: 0;
            transition: var(--transition);
        }

        .project-card:hover .project-img {
            transform: scale(1.1);
        }

        .project-card:hover .project-overlay {
            opacity: 1;
        }

        .project-title {
            font-size: 1.5rem;
            color: #fff;
            transform: translateY(20px);
            transition: var(--transition);
        }

        .project-category {
            color: var(--primary);
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
            transform: translateY(20px);
            transition: var(--transition);
            transition-delay: 0.1s;
        }

        .project-card:hover .project-title,
        .project-card:hover .project-category {
            transform: translateY(0);
        }

        /* About Section */
        .about {
            display: flex;
            align-items: center;
            gap: 4rem;
        }

        .about-content {
            flex: 1;
        }

        .about-img-wrap {
            flex: 1;
            position: relative;
        }

        .about-img {
            width: 100%;
            border-radius: 8px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }

        .experience-badge {
            position: absolute;
            bottom: -30px;
            right: -30px;
            background: var(--primary);
            color: #000;
            padding: 2rem;
            border-radius: 8px;
            text-align: center;
            font-family: var(--font-heading);
            font-weight: 800;
        }

        .experience-badge span {
            display: block;
            font-size: 3rem;
            line-height: 1;
        }

        /* Contact Section */
        .contact {
            background-color: var(--surface);
        }

        .contact-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
        }

        .contact-info h3 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
        }

        .contact-info p {
            color: var(--text-muted);
            margin-bottom: 2rem;
        }

        .info-item {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .info-icon {
            width: 50px;
            height: 50px;
            background: var(--surface-light);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary);
            font-size: 1.2rem;
        }

        .contact-form {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 1rem;
            background: var(--bg-color);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 4px;
            color: var(--text-main);
            font-family: var(--font-body);
            transition: var(--transition);
        }

        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: var(--primary);
        }

        .form-group textarea {
            height: 150px;
            resize: vertical;
        }

        /* Footer */
        .footer {
            background-color: #050505;
            padding: 4rem 0 2rem;
            border-top: 1px solid rgba(255,255,255,0.05);
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr;
            gap: 3rem;
            margin-bottom: 3rem;
        }

        .footer-logo {
            font-family: var(--font-heading);
            font-size: 1.8rem;
            font-weight: 800;
            margin-bottom: 1rem;
            display: block;
        }

        .footer-logo span {
            color: var(--primary);
        }

        .footer-desc {
            color: var(--text-muted);
            max-width: 400px;
        }

        .footer-heading {
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
        }

        .footer-links li {
            margin-bottom: 0.8rem;
        }

        .footer-links a {
            color: var(--text-muted);
            transition: var(--transition);
        }

        .footer-links a:hover {
            color: var(--primary);
        }

        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid rgba(255,255,255,0.05);
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        /* Animations */
        @keyframes fadeUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .animate-on-scroll {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.8s ease, transform 0.8s ease;
        }

        .animate-on-scroll.is-visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Responsive */
        @media (max-width: 992px) {
            .hero-title {
                font-size: 3.5rem;
            }
            .about {
                flex-direction: column;
            }
            .contact-container {
                grid-template-columns: 1fr;
            }
            .experience-badge {
                right: 0;
                bottom: -20px;
            }
            .footer-grid {
                grid-template-columns: 1fr 1fr;
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 0;
                right: -100%;
                height: 100vh;
                width: 70%;
                background: var(--surface);
                flex-direction: column;
                justify-content: center;
                align-items: center;
                transition: right 0.4s ease;
            }
            .nav-links.active {
                right: 0;
                box-shadow: -10px 0 30px rgba(0,0,0,0.5);
            }
            .menu-toggle {
                display: flex;
                z-index: 1001;
            }
            .menu-toggle.active span:nth-child(1) {
                transform: translateY(8px) rotate(45deg);
            }
            .menu-toggle.active span:nth-child(2) {
                opacity: 0;
            }
            .menu-toggle.active span:nth-child(3) {
                transform: translateY(-8px) rotate(-45deg);
            }
            .hero-title {
                font-size: 2.5rem;
            }
            .hero-desc {
                font-size: 1rem;
            }
            .footer-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="container nav-container">
            <a href="#" class="logo">PB<span>S</span>.</a>
            <div class="nav-links" id="nav-links">
                <a href="#home" class="active">Home</a>
                <a href="#about">About</a>
                <a href="#services">Services</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </div>
            <div class="menu-toggle" id="mobile-menu">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="container hero-content">
            <h1 class="hero-title">Building The Future With <span>Precision.</span></h1>
            <p class="hero-desc">PBS Construction delivers industry-leading commercial and residential projects. Quality craftsmanship, sustainable practices, and unwavering commitment to excellence.</p>
            <div class="hero-btns">
                <a href="#projects" class="btn btn-primary">Our Projects</a>
                <a href="#contact" class="btn btn-outline">Get a Quote</a>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="section container about" id="about">
        <div class="about-content animate-on-scroll">
            <span class="section-subtitle">About Us</span>
            <h2 class="section-title" style="margin-bottom: 1.5rem;">We Build Structures That Last Generations</h2>
            <p style="color: var(--text-muted); margin-bottom: 1.5rem;">At PBS Construction, we blend innovative engineering with time-honored craftsmanship. For decades, we have been the trusted partner for transforming ambitious blueprints into monumental realities.</p>
            <p style="color: var(--text-muted); margin-bottom: 2rem;">Our dedicated team of professionals ensures every project is completed on time, within budget, and to the highest standards of safety and quality.</p>
            <ul style="margin-bottom: 2rem;">
                <li style="margin-bottom: 0.5rem; display: flex; align-items: center; gap: 10px;">
                    <span style="color: var(--primary);">✓</span> Award-winning designs
                </li>
                <li style="margin-bottom: 0.5rem; display: flex; align-items: center; gap: 10px;">
                    <span style="color: var(--primary);">✓</span> Sustainable construction practices
                </li>
                <li style="display: flex; align-items: center; gap: 10px;">
                    <span style="color: var(--primary);">✓</span> 100% Client Satisfaction
                </li>
            </ul>
            <a href="#contact" class="btn btn-primary">Learn More</a>
        </div>
        <div class="about-img-wrap animate-on-scroll">
            <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?q=80&w=2062&auto=format&fit=crop" alt="Construction Site" class="about-img">
            <div class="experience-badge">
                <span>25+</span>
                Years Experience
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="section services" id="services">
        <div class="container">
            <div class="section-header animate-on-scroll">
                <span class="section-subtitle">Our Expertise</span>
                <h2 class="section-title">Comprehensive Construction Services</h2>
            </div>
            <div class="services-grid">
                <!-- Service 1 -->
                <div class="service-card animate-on-scroll">
                    <div class="service-icon">🏗️</div>
                    <h3 class="service-title">Commercial Construction</h3>
                    <p class="service-desc">State-of-the-art office buildings, retail spaces, and industrial facilities built to elevate your business operations.</p>
                </div>
                <!-- Service 2 -->
                <div class="service-card animate-on-scroll" style="transition-delay: 0.1s;">
                    <div class="service-icon">🏠</div>
                    <h3 class="service-title">Residential Developments</h3>
                    <p class="service-desc">Luxury homes and multi-family residential complexes designed for modern living and ultimate comfort.</p>
                </div>
                <!-- Service 3 -->
                <div class="service-card animate-on-scroll" style="transition-delay: 0.2s;">
                    <div class="service-icon">🔧</div>
                    <h3 class="service-title">Renovation & Remodeling</h3>
                    <p class="service-desc">Transforming existing structures with structural upgrades, aesthetic improvements, and energy-efficient retrofits.</p>
                </div>
                <!-- Service 4 -->
                <div class="service-card animate-on-scroll" style="transition-delay: 0.3s;">
                    <div class="service-icon">📐</div>
                    <h3 class="service-title">Architecture & Design</h3>
                    <p class="service-desc">End-to-end design-build services, ensuring seamless integration from conceptual sketches to final construction.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section class="section projects" id="projects">
        <div class="container">
            <div class="section-header animate-on-scroll">
                <span class="section-subtitle">Featured Work</span>
                <h2 class="section-title">Our Signature Projects</h2>
            </div>
            <div class="projects-grid">
                <!-- Project 1 -->
                <div class="project-card animate-on-scroll">
                    <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070&auto=format&fit=crop" alt="Skyline Tower" class="project-img">
                    <div class="project-overlay">
                        <span class="project-category">Commercial</span>
                        <h3 class="project-title">The Skyline Corporate Tower</h3>
                    </div>
                </div>
                <!-- Project 2 -->
                <div class="project-card animate-on-scroll" style="transition-delay: 0.1s;">
                    <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=2075&auto=format&fit=crop" alt="Modern Villa" class="project-img">
                    <div class="project-overlay">
                        <span class="project-category">Residential</span>
                        <h3 class="project-title">Azure Hills Villa Complex</h3>
                    </div>
                </div>
                <!-- Project 3 -->
                <div class="project-card animate-on-scroll" style="transition-delay: 0.2s;">
                    <img src="https://images.unsplash.com/photo-1516880711640-ef7daf81fc85?q=80&w=2059&auto=format&fit=crop" alt="Bridge Construction" class="project-img">
                    <div class="project-overlay">
                        <span class="project-category">Infrastructure</span>
                        <h3 class="project-title">Metro Link Suspension Bridge</h3>
                    </div>
                </div>
                <!-- Project 4 -->
                <div class="project-card animate-on-scroll" style="transition-delay: 0.3s;">
                    <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2069&auto=format&fit=crop" alt="Interior Office" class="project-img">
                    <div class="project-overlay">
                        <span class="project-category">Renovation</span>
                        <h3 class="project-title">Tech Hub Headquarters</h3>
                    </div>
                </div>
            </div>
            <div style="text-align: center; margin-top: 3rem;" class="animate-on-scroll">
                <a href="#" class="btn btn-outline">View All Projects</a>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="section container contact" id="contact">
        <div class="contact-container">
            <div class="contact-info animate-on-scroll">
                <span class="section-subtitle">Get In Touch</span>
                <h3>Ready to start your next big project?</h3>
                <p>Contact PBS Construction today. Our team of experts is ready to discuss your vision and provide a comprehensive proposal.</p>
                
                <div class="info-item">
                    <div class="info-icon">📍</div>
                    <div>
                        <h4 style="margin-bottom: 0.2rem;">Head Office</h4>
                        <span style="color: var(--text-muted);">123 Builder's Avenue, NY 10012, USA</span>
                    </div>
                </div>
                <div class="info-item">
                    <div class="info-icon">📞</div>
                    <div>
                        <h4 style="margin-bottom: 0.2rem;">Phone</h4>
                        <span style="color: var(--text-muted);">+1 (555) 123-4567</span>
                    </div>
                </div>
                <div class="info-item">
                    <div class="info-icon">✉️</div>
                    <div>
                        <h4 style="margin-bottom: 0.2rem;">Email</h4>
                        <span style="color: var(--text-muted);">contact@pbsconstruction.com</span>
                    </div>
                </div>
            </div>
            
            <div class="contact-form animate-on-scroll" style="transition-delay: 0.2s;">
                <form onsubmit="event.preventDefault(); alert('Message sent successfully! We will get back to you soon.');">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
                        <div class="form-group">
                            <input type="text" placeholder="First Name" required>
                        </div>
                        <div class="form-group">
                            <input type="text" placeholder="Last Name" required>
                        </div>
                    </div>
                    <div class="form-group" style="margin-bottom: 1.5rem;">
                        <input type="email" placeholder="Email Address" required>
                    </div>
                    <div class="form-group" style="margin-bottom: 1.5rem;">
                        <input type="text" placeholder="Project Subject" required>
                    </div>
                    <div class="form-group" style="margin-bottom: 1.5rem;">
                        <textarea placeholder="Tell us about your project details..." required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary" style="width: 100%;">Send Message</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <a href="#" class="footer-logo">PB<span>S</span>.</a>
                    <p class="footer-desc">Excellence in construction, driven by innovation, sustainability, and unparalleled craftsmanship since 1998.</p>
                </div>
                <div>
                    <h4 class="footer-heading">Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="#home">Home</a></li>
                        <li><a href="#about">About Us</a></li>
                        <li><a href="#services">Our Services</a></li>
                        <li><a href="#projects">Projects</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="footer-heading">Services</h4>
                    <ul class="footer-links">
                        <li><a href="#">Commercial</a></li>
                        <li><a href="#">Residential</a></li>
                        <li><a href="#">Renovation</a></li>
                        <li><a href="#">Architecture</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; <script>document.write(new Date().getFullYear())</script> PBS Construction. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- JavaScript for Interactivity -->
    <script>
        // Navbar Scroll Effect
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Mobile Menu Toggle
        const mobileMenu = document.getElementById('mobile-menu');
        const navLinks = document.getElementById('nav-links');
        
        mobileMenu.addEventListener('click', () => {
            mobileMenu.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        // Close mobile menu on link click
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });

        // Active Link Highlighting
        const sections = document.querySelectorAll('section');
        const navItems = document.querySelectorAll('.nav-links a');

        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (pageYOffset >= (sectionTop - sectionHeight / 3)) {
                    current = section.getAttribute('id');
                }
            });

            navItems.forEach(item => {
                item.classList.remove('active');
                if (item.getAttribute('href').slice(1) === current) {
                    item.classList.add('active');
                }
            });
        });

        // Scroll Animation (Intersection Observer)
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.15
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target); // Optional: stop observing once animated
                }
            });
        }, observerOptions);

        document.querySelectorAll('.animate-on-scroll').forEach((elem) => {
            observer.observe(elem);
        });
    </script>

    <!-- Three.js and Vanta.js for Building Animation Background -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.buildings.min.js"></script>
    <script>
        // Initialize Vanta Buildings on the Hero Section
        VANTA.BUILDINGS({
            el: "#home",
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x00F2FF,       // Cyan/Teal like Cognizance
            backgroundColor: 0x000B1A // Dark blue deep space like Cognizance
        });
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    gg = request.args.get('gg', 'Not Provided')
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', 'Unknown')
    return render_template_string(HTML, gg=gg, name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
