import os
import json
import re

PARSED_DIR = r"c:\Users\pawan\Videos\Ash&Sims\raw_html\parsed"
OUTPUT_DIR = r"c:\Users\pawan\Videos\Ash&Sims"

# Load image mapping
with open(os.path.join(r"c:\Users\pawan\Videos\Ash&Sims\raw_html", "image_mapping.json"), 'r') as f:
    img_map = json.load(f)

# Resolve image URL helper
def resolve_img(url):
    if not url:
        return ""
    # Check if url in mapping
    if url in img_map:
        return img_map[url]
    # Check if a partial match or filename matches
    filename = os.path.basename(url)
    for orig_url, local_path in img_map.items():
        if filename == os.path.basename(orig_url):
            return local_path
    # Fallback to local image path
    return f"/assets/images/{filename}"

def get_shared_header(title, description, relative_depth=0):
    root_prefix = "../" * relative_depth
    
    # Generate navigation links based on depth
    home_url = root_prefix + "index.html"
    about_url = root_prefix + "about/index.html"
    services_url = root_prefix + "services/index.html"
    clients_url = root_prefix + "clients/index.html"
    blog_url = root_prefix + "blog/index.html"
    contact_url = root_prefix + "contact/index.html"
    
    # Sub-services links
    vb_url = root_prefix + "services/large-format-digital-printing/vehicle-branding/index.html"
    lf_url = root_prefix + "services/large-format-digital-printing/index.html"
    fab_url = root_prefix + "services/fabrication/index.html"
    flag_url = root_prefix + "services/flags-fabric-printing/index.html"
    sig_url = root_prefix + "services/signage/index.html"
    corp_url = root_prefix + "services/corporate-gifts/index.html"
    des_url = root_prefix + "services/designing/index.html"
    off_url = root_prefix + "services/offset-printing/index.html"

    logo_path = root_prefix + "assets/images/logo.png"
    favicon_path = root_prefix + "assets/images/favicon.png"
    style_path = root_prefix + "style.css"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="icon" type="image/png" href="{favicon_path}">
    <link rel="stylesheet" href="{style_path}">
    <!-- FontAwesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="{home_url}" class="logo">
                <img src="{logo_path}" alt="Ash & Sims Advertising LLC">
            </a>
            
            <button class="mobile-nav-toggle" aria-label="Toggle Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            
            <nav class="nav">
                <ul class="nav-list">
                    <li><a href="{home_url}" class="nav-link">Home</a></li>
                    <li><a href="{about_url}" class="nav-link">About</a></li>
                    <li class="nav-item-dropdown">
                        <a href="{services_url}" class="nav-link">Services <i class="fa fa-angle-down"></i></a>
                        <div class="nav-dropdown">
                            <a href="{vb_url}" class="dropdown-link">Vehicle Branding</a>
                            <a href="{lf_url}" class="dropdown-link">Large Format Printing</a>
                            <a href="{fab_url}" class="dropdown-link">Fabrication</a>
                            <a href="{flag_url}" class="dropdown-link">Flags & Fabric Printing</a>
                            <a href="{sig_url}" class="dropdown-link">Signage</a>
                            <a href="{corp_url}" class="dropdown-link">Corporate Gifts</a>
                            <a href="{des_url}" class="dropdown-link">Designing</a>
                            <a href="{off_url}" class="dropdown-link">Offset Printing</a>
                        </div>
                    </li>
                    <li><a href="{clients_url}" class="nav-link">Clients</a></li>
                    <li><a href="{blog_url}" class="nav-link">Blog</a></li>
                    <li><a href="{contact_url}" class="nav-link">Contact</a></li>
                </ul>
            </nav>
            
            <div class="nav-cta">
                <a href="{contact_url}" class="btn btn-primary">Get a Quote</a>
            </div>
        </div>
    </header>
"""

def get_shared_footer(relative_depth=0, include_ecommerce=False):
    root_prefix = "../" * relative_depth
    home_url = root_prefix + "index.html"
    about_url = root_prefix + "about/index.html"
    services_url = root_prefix + "services/index.html"
    clients_url = root_prefix + "clients/index.html"
    blog_url = root_prefix + "blog/index.html"
    contact_url = root_prefix + "contact/index.html"
    
    logo_footer_path = root_prefix + "assets/images/logo-footer.png"
    main_js_path = root_prefix + "main.js"

    return f"""
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <div class="footer-logo">
                        <img src="{logo_footer_path}" alt="Ash & Sims Logo">
                    </div>
                    <p class="footer-about-text">
                        Ash & Sims is one of the leading large format digital printing, signage & corporate gifts companies in Dubai, UAE. We offer complete visual merchandising solutions with exceptional service at reasonable prices.
                    </p>
                    <div class="footer-socials">
                        <a href="https://www.facebook.com/Ash-Sims-Advertising-LLC-233149380044946" target="_blank" class="footer-social-icon"><i class="fab fa-facebook-f"></i></a>
                        <a href="https://www.linkedin.com/company/ash-&-sims-advertising/about/" target="_blank" class="footer-social-icon"><i class="fab fa-linkedin-in"></i></a>
                        <a href="https://www.instagram.com/ashandsimsadvt/" target="_blank" class="footer-social-icon"><i class="fab fa-instagram"></i></a>
                        <a href="https://wa.link/h6cjuj" target="_blank" class="footer-social-icon"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
                
                <div class="footer-col">
                    <h4 class="footer-links-title">Quick Links</h4>
                    <ul class="footer-links-list">
                        <li><a href="{home_url}">Home</a></li>
                        <li><a href="{about_url}">About Us</a></li>
                        <li><a href="{services_url}">Our Services</a></li>
                        <li><a href="{clients_url}">Our Clients</a></li>
                        <li><a href="{blog_url}">Blog</a></li>
                        <li><a href="{contact_url}">Contact Us</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h4 class="footer-links-title">Services</h4>
                    <ul class="footer-links-list">
                        <li><a href="{root_prefix}services/large-format-digital-printing/vehicle-branding/index.html">Vehicle Branding</a></li>
                        <li><a href="{root_prefix}services/large-format-digital-printing/index.html">Large Format Printing</a></li>
                        <li><a href="{root_prefix}services/fabrication/index.html">Exhibition & Fabrication</a></li>
                        <li><a href="{root_prefix}services/flags-fabric-printing/index.html">Flags & Fabric</a></li>
                        <li><a href="{root_prefix}services/signage/index.html">Signage Manufacturing</a></li>
                        <li><a href="{root_prefix}services/corporate-gifts/index.html">Corporate Gifts</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h4 class="footer-links-title">Contact Info</h4>
                    <ul class="contact-info-list" style="margin-top:0;">
                        <li class="contact-info-item">
                            <i class="fa fa-map-marker-alt contact-info-icon" style="color:var(--color-primary);"></i>
                            <div class="contact-info-text">
                                <p style="color:#ffffff; font-weight:600; margin-bottom: 2px;">Address</p>
                                <p style="color:rgba(255,255,255,0.7); font-size:0.85rem;">P.O Box 117822, Dubai, United Arab Emirates</p>
                            </div>
                        </li>
                        <li class="contact-info-item">
                            <i class="fa fa-phone-alt contact-info-icon" style="color:var(--color-primary);"></i>
                            <div class="contact-info-text">
                                <p style="color:#ffffff; font-weight:600; margin-bottom: 2px;">Phone</p>
                                <p style="color:rgba(255,255,255,0.7); font-size:0.85rem;">+971 55 415 1136</p>
                            </div>
                        </li>
                        <li class="contact-info-item">
                            <i class="fa fa-envelope contact-info-icon" style="color:var(--color-primary);"></i>
                            <div class="contact-info-text">
                                <p style="color:#ffffff; font-weight:600; margin-bottom: 2px;">Email</p>
                                <p style="color:rgba(255,255,255,0.7); font-size:0.85rem;">info@ashandsims.com</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-copyright">
                <p>&copy; {2026} Ash & Sims Advertising LLC. All Rights Reserved. Built with modern, flexible design systems.</p>
            </div>
        </div>
    </footer>
    
    <!-- Floating Widgets -->
    <div class="floating-widget">
        <a href="https://wa.me/971554151136" target="_blank" class="float-btn float-whatsapp" aria-label="Chat on WhatsApp">
            <i class="fab fa-whatsapp"></i>
        </a>
        <a href="tel:+971554151136" class="float-btn float-phone" aria-label="Call Us">
            <i class="fa fa-phone"></i>
        </a>
    </div>
    
    <script type="module" src="{main_js_path}"></script>
    {" " if not include_ecommerce else f'<script type="module" src="{root_prefix}ecommerce.js"></script>' }
</body>
</html>
"""

def generate_breadcrumbs(current_page, relative_depth=0):
    root_prefix = "../" * relative_depth
    home_link = f'<a href="{root_prefix}index.html">Home</a>'
    return f"""
    <div class="breadcrumbs">
        {home_link} &raquo; <span>{current_page}</span>
    </div>
    """

# 1. COMPILE HOME PAGE (index.html)
def compile_home():
    with open(os.path.join(PARSED_DIR, "home_parsed.json"), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    title = data['title']
    desc = data['description']
    
    hero_img = resolve_img("https://www.ashandsims.com/wp-content/uploads/2022/03/digital-printing-company-in-dubai.jpg")
    
    body = f"""
    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-grid">
                <div class="hero-content">
                    <h1 class="hero-title">Printing & Vehicle Branding in Dubai</h1>
                    <p class="hero-desc">
                        Ash & Sims is one of the leading large format digital printing, signage & corporate gifts companies in Dubai. We offer exceptional prints, low prices, and fast deliveries.
                    </p>
                    <div class="hero-actions">
                        <a href="services/index.html" class="btn btn-primary">Explore Services</a>
                        <a href="contact/index.html" class="btn btn-outline">Get a Quote</a>
                    </div>
                </div>
                <div class="hero-image-wrap">
                    <img class="hero-image" src="{hero_img}" alt="Digital Printing Company in Dubai">
                </div>
            </div>
        </div>
    </section>
    
    <!-- Core Value Cards -->
    <section class="section" style="padding-top:0;">
        <div class="container">
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon"><i class="fa fa-clock"></i></div>
                    <h3 class="feature-title">Punctuality</h3>
                    <p class="feature-desc">We are never late! With us, you can rest assured your product delivery will be timely and hassle-free.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon"><i class="fa fa-certificate"></i></div>
                    <h3 class="feature-title">Professional Applicators</h3>
                    <p class="feature-desc">Highly experienced, well-trained, and certified applicators team to serve your custom branding needs.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon"><i class="fa fa-tags"></i></div>
                    <h3 class="feature-title">Competitive Pricing</h3>
                    <p class="feature-desc">Our long years of industry experience allow us to offer the most competitive prices in the UAE market.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Overview Section -->
    <section class="section" style="background-color:#ffffff;">
        <div class="container">
            <div class="section-header">
                <span class="section-subtitle">What We Offer</span>
                <h2 class="section-title">Our Premium Services</h2>
                <p class="section-desc">We offer a complete array of digital printing, advertising, fabrication, flags, signage, corporate gifts, and graphic design solutions under one roof.</p>
            </div>
            
            <div class="services-grid">
                <!-- Service 1: Vehicle Branding -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Vehicle-Branding-01.jpg")}" alt="Vehicle Branding">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Vehicle Branding</h3>
                        <p class="service-card-desc">Convert your daily commute to advertise your products. Vehicle wraps are the most cost-effective advertisement tool for business.</p>
                        <a href="services/large-format-digital-printing/vehicle-branding/index.html" class="service-card-link">Read More <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 2: Large Format Printing -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/02/large-format-digital-printing.jpg")}" alt="Large Format Printing">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Large Format Digital Printing</h3>
                        <p class="service-card-desc">Banners, backlit flex, banners, floor stickers, posters, rollups, wall & glass graphics with sharp, vibrant outputs.</p>
                        <a href="services/large-format-digital-printing/index.html" class="service-card-link">Read More <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 3: Fabrication -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Exhibition-Stands-01.jpg")}" alt="Fabrication">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Exhibition & Fabrication</h3>
                        <p class="service-card-desc">Exhibition stands, kiosks, podiums, promotional tables, FSDU units, and custom retail pop-up activations.</p>
                        <a href="services/fabrication/index.html" class="service-card-link">Read More <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 4: Flags & Fabric Printing -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Teardrop-Flags-02.jpg")}" alt="Flags Printing">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Flags & Fabric Printing</h3>
                        <p class="service-card-desc">High-quality dye-sublimation flag printing, telescopic flags, teardrop flags, custom tents, and beach umbrellas.</p>
                        <a href="services/flags-fabric-printing/index.html" class="service-card-link">Read More <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 5: Signage -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Signage-03.jpg")}" alt="Signage">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Signage Manufacturing</h3>
                        <p class="service-card-desc">Unique design and top-quality internal & external signage boards that distinguish your brand from the rest.</p>
                        <a href="services/signage/index.html" class="service-card-link">Read More <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 6: Corporate Gifts -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Pens-03.jpg")}" alt="Corporate Gifts">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Corporate Gifts</h3>
                        <p class="service-card-desc">Improve customer relationships with customized promotional gifts like pens, diaries, shirts, USBs, and caps.</p>
                        <a href="services/corporate-gifts/index.html" class="service-card-link">Read More <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Clients Showcase -->
    <section class="section">
        <div class="container">
            <div class="section-header">
                <span class="section-subtitle">Trusted By Major Brands</span>
                <h2 class="section-title">Our Valued Clients</h2>
                <p class="section-desc">Over the years, we have partnered with major global brands and local businesses to fulfill their branding objectives.</p>
            </div>
            
            <div class="client-logos">
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Access.jpg")}" alt="Access"></div>
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Al-Jazira.jpg")}" alt="Al Jazira"></div>
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Al-Maya.jpg")}" alt="Al Maya"></div>
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Datar.jpg")}" alt="Datar"></div>
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Fitflop.jpg")}" alt="Fitflop"></div>
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/GSL.jpg")}" alt="GSL"></div>
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Original.jpg")}" alt="Original"></div>
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Rise.jpg")}" alt="Rise"></div>
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Wow.jpg")}" alt="Wow"></div>
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/VOX-Cinemas.jpg")}" alt="VOX Cinemas"></div>
                <div class="client-logo-item"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Transcorp.jpg")}" alt="Transcorp"></div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
        <div class="container">
            <h2 class="cta-title">Need Eye-Catching Branding & Printing Solutions?</h2>
            <p class="cta-desc">Partner with Ash & Sims today to transform your business's visual merchandising identity. Contact us for custom quotes.</p>
            <a href="contact/index.html" class="btn btn-white">Contact Us Now</a>
        </div>
    </section>
    """
    
    html = get_shared_header(title, desc, 0) + body + get_shared_footer(0)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Compiled index.html")

# 2. COMPILE ABOUT PAGE (about/index.html)
def compile_about():
    with open(os.path.join(PARSED_DIR, "about_parsed.json"), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    title = data['title']
    desc = data['description']
    
    os.makedirs(os.path.join(OUTPUT_DIR, "about"), exist_ok=True)
    
    body = f"""
    <!-- Page Header -->
    <section class="page-header">
        <div class="container">
            <h1 class="page-header-title">About Ash & Sims</h1>
            {generate_breadcrumbs("About", 1)}
        </div>
    </section>

    <!-- Main Content Section -->
    <section class="section" style="background-color:#ffffff;">
        <div class="container">
            <div style="max-width: 900px; margin: 0 auto;">
                <h2 style="font-size:2.25rem; margin-bottom: 24px; color:var(--color-dark);">Leading Large Format Digital Printing Company</h2>
                <p style="font-size:1.1rem; line-height:1.8; color:#374151; margin-bottom: 20px;">
                    Ash & Sims has established itself as one of the leading providers of digital printing, signage & corporate gifts. Since our inception in 2007, the company has always strived to provide complete visual merchandising solutions with exceptional service at reasonable prices, and this value continues to drive the business forward.
                </p>
                <p style="font-size:1.1rem; line-height:1.8; color:#374151; margin-bottom: 20px;">
                    We are a one-stop shop for all the digital printing and branding needs of businesses. We offer a complete array of products and services related to visual merchandising, branding, signage, and corporate gifts under one roof. Whether you are looking for simple roll-up/pop-up banners or elaborate product launch visual planning, we give attention to detail to achieve the desired objective.
                </p>
                <p style="font-size:1.15rem; font-weight:600; color:var(--color-primary); border-left:4px solid var(--color-primary); padding-left:20px; margin: 30px 0;">
                    "Our USP is providing cost-effective solutions with uncompromising quality."
                </p>
            </div>
        </div>
    </section>

    <!-- Mission & Vision Section -->
    <section class="section" style="background-color:var(--color-light);">
        <div class="container">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:50px;">
                <div class="feature-card" style="padding:40px;">
                    <div class="feature-icon"><i class="fa fa-bullseye"></i></div>
                    <h3 class="feature-title" style="font-size:1.5rem; margin-bottom:15px;">Our Mission</h3>
                    <p class="feature-desc" style="font-size:1.05rem;">Our mission is to stand out from the clutter by understanding our client's requirements, building innovative solutions, and exceeding customer satisfaction with exceptional execution.</p>
                </div>
                <div class="feature-card" style="padding:40px;">
                    <div class="feature-icon"><i class="fa fa-eye"></i></div>
                    <h3 class="feature-title" style="font-size:1.5rem; margin-bottom:15px;">Our Vision</h3>
                    <p class="feature-desc" style="font-size:1.05rem;">Our vision is to be a market leader in being a complete visual merchandising solutions and corporate gifts company in the UAE. We aim for continuous improvement and customer delight.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Company Strengths -->
    <section class="section" style="background-color:#ffffff;">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Why Partner With Us?</h2>
                <p class="section-desc">Our key values and operations make us the preferred partner for leading agencies and brands.</p>
            </div>
            
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:30px;">
                <div style="padding:24px; border:1px solid var(--color-border); border-radius:12px;">
                    <h4 style="font-size:1.2rem; color:var(--color-primary); margin-bottom:12px;">Dedicated Team</h4>
                    <p style="color:var(--color-text-muted); font-size:0.95rem;">Our key strength is our hard-working and dedicated team. They are the backbone of our company, ready to handle large or complicated setups.</p>
                </div>
                <div style="padding:24px; border:1px solid var(--color-border); border-radius:12px;">
                    <h4 style="font-size:1.2rem; color:var(--color-primary); margin-bottom:12px;">Strict Punctuality</h4>
                    <p style="color:var(--color-text-muted); font-size:0.95rem;">We are never late! With us, you can rest assured your product delivery will be timely. We understand that time is critical for marketing campaigns.</p>
                </div>
                <div style="padding:24px; border:1px solid var(--color-border); border-radius:12px;">
                    <h4 style="font-size:1.2rem; color:var(--color-primary); margin-bottom:12px;">Professionalism</h4>
                    <p style="color:var(--color-text-muted); font-size:0.95rem;">We have a highly experienced, well-trained and 3M & Orafol Certified applicators team to serve you the best for vehicle branding and wraps.</p>
                </div>
                <div style="padding:24px; border:1px solid var(--color-border); border-radius:12px;">
                    <h4 style="font-size:1.2rem; color:var(--color-primary); margin-bottom:12px;">Comprehensive Solutions</h4>
                    <p style="color:var(--color-text-muted); font-size:0.95rem;">We offer a vast array of services under one roof. We cater to all your design, printing, sign board manufacturing, and corporate gift needs.</p>
                </div>
            </div>
        </div>
    </section>
    """
    
    html = get_shared_header(title, desc, 1) + body + get_shared_footer(1)
    with open(os.path.join(OUTPUT_DIR, "about/index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Compiled about/index.html")

# 3. COMPILE CONTACT PAGE (contact/index.html)
def compile_contact():
    with open(os.path.join(PARSED_DIR, "contact_parsed.json"), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    title = data['title']
    desc = data['description']
    
    os.makedirs(os.path.join(OUTPUT_DIR, "contact"), exist_ok=True)
    
    body = f"""
    <!-- Page Header -->
    <section class="page-header">
        <div class="container">
            <h1 class="page-header-title">Contact Us</h1>
            {generate_breadcrumbs("Contact", 1)}
        </div>
    </section>

    <!-- Contact details section -->
    <section class="section" style="background-color:#ffffff;">
        <div class="container">
            <div class="contact-grid">
                <div class="contact-form-card">
                    <h3 style="font-size:1.75rem; margin-bottom:15px; color:var(--color-dark);">Send Us a Message</h3>
                    <p style="color:var(--color-text-muted); margin-bottom:30px;">Do you have a project or query in mind? Fill out the form and our representative will reach out to you within 24 hours.</p>
                    
                    <form id="contact-form">
                        <div class="form-group">
                            <label class="form-label" for="name">Your Name *</label>
                            <input class="form-input" type="text" id="name" required placeholder="John Doe">
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="email">Your Email *</label>
                            <input class="form-input" type="email" id="email" required placeholder="john@example.com">
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="phone">Phone Number *</label>
                            <input class="form-input" type="tel" id="phone" required placeholder="+971 50 123 4567">
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="service">Select Service</label>
                            <input class="form-input" type="text" id="service" placeholder="e.g. Vehicle Branding, Signage">
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="message">Message *</label>
                            <textarea class="form-textarea" id="message" required placeholder="Describe your printing/branding needs..."></textarea>
                        </div>
                        <button class="btn btn-primary" type="submit" style="width:100%;">Submit Inquiry</button>
                    </form>
                </div>
                
                <div class="sidebar">
                    <div class="sidebar-widget contact-widget">
                        <h3 class="widget-title">Get In Touch</h3>
                        <ul class="contact-info-list">
                            <li class="contact-info-item">
                                <i class="fa fa-map-marker-alt contact-info-icon"></i>
                                <div class="contact-info-text">
                                    <h4>Office Address</h4>
                                    <p>Ash & Sims Advertising LLC<br>P.O Box 117822, Dubai, United Arab Emirates</p>
                                </div>
                            </li>
                            <li class="contact-info-item">
                                <i class="fa fa-phone-alt contact-info-icon"></i>
                                <div class="contact-info-text">
                                    <h4>Direct Call / Support</h4>
                                    <p>+971 55 415 1136</p>
                                </div>
                            </li>
                            <li class="contact-info-item">
                                <i class="fa fa-envelope contact-info-icon"></i>
                                <div class="contact-info-text">
                                    <h4>Email Address</h4>
                                    <p>info@ashandsims.com</p>
                                </div>
                            </li>
                            <li class="contact-info-item">
                                <i class="fab fa-whatsapp contact-info-icon"></i>
                                <div class="contact-info-text">
                                    <h4>WhatsApp</h4>
                                    <p>+971 55 415 1136</p>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Map Container -->
            <div class="map-container">
                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d115518.23275713437!2d55.195973789062494!3d25.19751480000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5f434b9d5c3fcf%3A0x67ee1c03e33e9d89!2sDubai!5e0!3m2!1sen!2sae!4v1622359489240!5m2!1sen!2sae" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
            </div>
        </div>
    </section>
    """
    
    html = get_shared_header(title, desc, 1) + body + get_shared_footer(1)
    with open(os.path.join(OUTPUT_DIR, "contact/index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Compiled contact/index.html")

# 4. COMPILE CLIENTS PAGE (clients/index.html)
def compile_clients():
    with open(os.path.join(PARSED_DIR, "clients_parsed.json"), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    title = data['title']
    desc = data['description']
    
    os.makedirs(os.path.join(OUTPUT_DIR, "clients"), exist_ok=True)
    
    body = f"""
    <!-- Page Header -->
    <section class="page-header">
        <div class="container">
            <h1 class="page-header-title">Our Clients</h1>
            {generate_breadcrumbs("Clients", 1)}
        </div>
    </section>

    <!-- Clients grid section -->
    <section class="section" style="background-color:#ffffff;">
        <div class="container">
            <div class="section-header">
                <span class="section-subtitle">Partnerships</span>
                <h2 class="section-title">Valued Brands We Serve</h2>
                <p class="section-desc">Over the years, we have delivered visual merchandising, digital printing, and signage systems for some of the biggest names in the UAE and internationally.</p>
            </div>
            
            <div class="client-logos" style="gap:60px; max-width: 900px; margin: 0 auto;">
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Access.jpg")}" alt="Access"></div>
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Al-Jazira.jpg")}" alt="Al Jazira"></div>
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Al-Maya.jpg")}" alt="Al Maya"></div>
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Datar.jpg")}" alt="Datar"></div>
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Fitflop.jpg")}" alt="Fitflop"></div>
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/GSL.jpg")}" alt="GSL"></div>
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Original.jpg")}" alt="Original"></div>
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Rise.jpg")}" alt="Rise"></div>
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/Wow.jpg")}" alt="Wow"></div>
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/01/VOX-Cinemas.jpg")}" alt="VOX Cinemas"></div>
                <div class="client-logo-item" style="width:160px; height:120px;"><img src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Transcorp.jpg")}" alt="Transcorp"></div>
            </div>
        </div>
    </section>
    """
    
    html = get_shared_header(title, desc, 1) + body + get_shared_footer(1)
    with open(os.path.join(OUTPUT_DIR, "clients/index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Compiled clients/index.html")

# 5. COMPILE SERVICES INDEX PAGE (services/index.html)
def compile_services_index():
    with open(os.path.join(PARSED_DIR, "services_parsed.json"), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    title = data['title']
    desc = data['description']
    
    os.makedirs(os.path.join(OUTPUT_DIR, "services"), exist_ok=True)
    
    body = f"""
    <!-- Page Header -->
    <section class="page-header">
        <div class="container">
            <h1 class="page-header-title">Our Services</h1>
            {generate_breadcrumbs("Services", 1)}
        </div>
    </section>

    <!-- Services Grid Section -->
    <section class="section" style="background-color:#ffffff;">
        <div class="container">
            <div class="services-grid" style="grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));">
                
                <!-- Service 1: Vehicle Branding -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Vehicle-Branding-01.jpg")}" alt="Vehicle Branding">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Vehicle Branding</h3>
                        <p class="service-card-desc">Car wrapping, van branding, van wraps, truck wraps, bus wrapping. Turn transport fleets into billboards.</p>
                        <a href="large-format-digital-printing/vehicle-branding/index.html" class="service-card-link">Explore Vehicle Branding <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 2: Large Format Printing -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/02/large-format-digital-printing.jpg")}" alt="Large Format Printing">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Large Format Digital Printing</h3>
                        <p class="service-card-desc">Backlit flex boards, vinyl stickers, banner graphics, rollup stands, wall graphics, glass branding, and posters.</p>
                        <a href="large-format-digital-printing/index.html" class="service-card-link">Explore Large Format Printing <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 3: Fabrication -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Exhibition-Stands-01.jpg")}" alt="Fabrication">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Fabrication & Exhibitions</h3>
                        <p class="service-card-desc">Exhibition stand design, kiosk fabrication, counter systems, FSDU retail racks, promotional display units.</p>
                        <a href="fabrication/index.html" class="service-card-link">Explore Fabrication <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 4: Flags & Fabric Printing -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Teardrop-Flags-02.jpg")}" alt="Flags Printing">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Flags & Fabric Printing</h3>
                        <p class="service-card-desc">Beach flags, teardrop flags, telescopic flag systems, canopy tents, umbrellas, Toblerone flags.</p>
                        <a href="flags-fabric-printing/index.html" class="service-card-link">Explore Flags & Fabric <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 5: Signage -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Signage-03.jpg")}" alt="Signage">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Signage Manufacturing</h3>
                        <p class="service-card-desc">3D letter signs, acrylic signs, neon signs, backlit internal and external building signage.</p>
                        <a href="signage/index.html" class="service-card-link">Explore Signage <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 6: Corporate Gifts -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Pens-03.jpg")}" alt="Corporate Gifts">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Corporate Gifts</h3>
                        <p class="service-card-desc">Pens, organizers, shirts & t-shirts, diaries, USB drives, custom gift items for promotion.</p>
                        <a href="corporate-gifts/index.html" class="service-card-link">Explore Corporate Gifts <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 7: Designing -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Designing-02.jpg")}" alt="Designing">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Designing</h3>
                        <p class="service-card-desc">Professional logo designing, layout designing, flyers, vector artworks, and corporate branding identity.</p>
                        <a href="designing/index.html" class="service-card-link">Explore Designing <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Service 8: Offset Printing -->
                <div class="service-card">
                    <div class="service-img-wrap">
                        <img class="service-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/06/Business-Cards-03.jpg")}" alt="Offset Printing">
                    </div>
                    <div class="service-content">
                        <h3 class="service-card-title">Offset Printing</h3>
                        <p class="service-card-desc">High-volume business cards, envelopes, flyers, folders, notepads, wobblers, danglers, shelf talkers.</p>
                        <a href="offset-printing/index.html" class="service-card-link">Explore Offset Printing <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

            </div>
        </div>
    </section>
    """
    
    html = get_shared_header(title, desc, 1) + body + get_shared_footer(1)
    with open(os.path.join(OUTPUT_DIR, "services/index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Compiled services/index.html")

# Helper to compile subservice pages
def compile_subservice(json_filename, subfolder_path, relative_depth, service_name, sidebar_active_index, gallery_imgs):
    with open(os.path.join(PARSED_DIR, json_filename), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    title = data['title']
    desc = data['description']
    
    os.makedirs(os.path.join(OUTPUT_DIR, subfolder_path), exist_ok=True)
    
    # Extract and build content dynamically
    html_elements = []
    in_list = False
    
    for el in data['elements']:
        tag = el['tag']
        text = el['text'].strip()
        
        # Skip breadcrumbs or header duplicates
        if '»' in text or '\u00bb' in text:
            continue
        if text.lower() == service_name.lower():
            continue
        if text.strip() == "KEY SERVICES":
            continue
            
        # Handle list items grouping
        if tag == 'li':
            if not in_list:
                html_elements.append("<ul style='margin-bottom: 24px; padding-left: 20px;'>")
                in_list = True
            html_elements.append(f"<li style='margin-bottom: 8px;'>{text}</li>")
        else:
            if in_list:
                html_elements.append("</ul>")
                in_list = False
            
            if tag in ['h2', 'h3', 'h4', 'h5', 'h6']:
                html_elements.append(f"<{tag} style='margin-top: 32px; margin-bottom: 16px; color:var(--color-dark);'>{text}</{tag}>")
            elif tag == 'p':
                html_elements.append(f"<p style='margin-bottom: 20px; line-height: 1.7; color:#374151;'>{text}</p>")
                
    if in_list:
        html_elements.append("</ul>")
        
    p_html = "\n".join(html_elements)
    
    main_image_url = ""
    # Find a good main image from elements/images
    if data['images']:
        main_image_url = resolve_img(data['images'][0]['src'])
    else:
        # Use first gallery image as fallback
        main_image_url = resolve_img(gallery_imgs[0]) if gallery_imgs else ""
    
    gallery_html = ""
    if gallery_imgs:
        gallery_items = "".join([f'<div class="gallery-item"><img src="{resolve_img(img)}" alt="Sample"></div>' for img in gallery_imgs])
        gallery_html = f"""
        <h3 style="font-size:1.5rem; margin-top: 40px; margin-bottom: 20px;">Work Gallery / Portfolio</h3>
        <div class="gallery-grid">
            {gallery_items}
        </div>
        """
        
    root_prefix = "../" * relative_depth
    
    sidebar_menu = f"""
    <ul class="services-list-widget">
        <li class="{"active" if sidebar_active_index == 1 else ""}"><a href="{root_prefix}services/large-format-digital-printing/vehicle-branding/index.html">Vehicle Branding</a></li>
        <li class="{"active" if sidebar_active_index == 2 else ""}"><a href="{root_prefix}services/large-format-digital-printing/index.html">Large Format Printing</a></li>
        <li class="{"active" if sidebar_active_index == 3 else ""}"><a href="{root_prefix}services/fabrication/index.html">Exhibition & Fabrication</a></li>
        <li class="{"active" if sidebar_active_index == 4 else ""}"><a href="{root_prefix}services/flags-fabric-printing/index.html">Flags & Fabric</a></li>
        <li class="{"active" if sidebar_active_index == 5 else ""}"><a href="{root_prefix}services/signage/index.html">Signage Manufacturing</a></li>
        <li class="{"active" if sidebar_active_index == 6 else ""}"><a href="{root_prefix}services/corporate-gifts/index.html">Corporate Gifts</a></li>
        <li class="{"active" if sidebar_active_index == 7 else ""}"><a href="{root_prefix}services/designing/index.html">Designing</a></li>
        <li class="{"active" if sidebar_active_index == 8 else ""}"><a href="{root_prefix}services/offset-printing/index.html">Offset Printing</a></li>
    </ul>
    """

    is_gifts = (service_name == "Corporate Gifts")
    
    if is_gifts:
        main_content_html = f"""
                <div class="service-detail-content">
                    <h2 style="font-size:2rem; margin-top:20px; margin-bottom:20px; color:var(--color-dark);">B2B Corporate Gifts Catalog</h2>
                    <p style="margin-bottom:30px; color:#374151; line-height:1.7;">
                        Welcome to the Ash & Sims wholesale gifting portal. Browse our curated selection of high-quality corporate giveaways. Filter by category, adjust bulk quantities to receive wholesale volume discounts dynamically, and request custom quotes with your logo engraving or printing specifications.
                    </p>
                    
                    <!-- Category Tabs -->
                    <div class="catalog-filters"></div>
                    
                    <!-- Products Grid -->
                    <div class="products-grid"></div>
                </div>
                
                <!-- Floating Cart Button -->
                <button class="cart-float-btn" aria-label="Open Quote Cart">
                    <i class="fa fa-shopping-basket"></i>
                    <span class="cart-badge-count">0</span>
                </button>
                
                <!-- Sidebar Cart Drawer -->
                <div class="cart-drawer-backdrop"></div>
                <div class="cart-drawer">
                    <div class="cart-drawer-header">
                        <h3 class="cart-drawer-title"><i class="fa fa-shopping-basket" style="color:var(--color-primary);"></i> B2B Quote Cart</h3>
                        <button class="cart-drawer-close" aria-label="Close Cart">&times;</button>
                    </div>
                    <div class="cart-drawer-body">
                        <!-- Rendered via JS -->
                    </div>
                    <div class="cart-drawer-footer">
                        <div class="cart-summary-row">
                            <span>Base Subtotal:</span>
                            <span class="cart-summary-subtotal-val">AED 0.00</span>
                        </div>
                        <div class="cart-summary-row">
                            <span>Volume Discount:</span>
                            <span class="cart-summary-discount-val" style="color:#25d366; font-weight:600;">0%</span>
                        </div>
                        <div class="cart-summary-row cart-summary-total">
                            <span>Estimated Total:</span>
                            <span class="cart-summary-total-val">AED 0.00</span>
                        </div>
                        <button class="btn btn-primary cart-checkout-btn" style="width:100%; margin-top:16px;" disabled>
                            <i class="fa fa-paper-plane"></i> Request B2B Quotation
                        </button>
                    </div>
                </div>
                
                <!-- RFQ Checkout Modal -->
                <div class="quote-modal-backdrop">
                    <div class="quote-modal">
                        <div class="quote-modal-header">
                            <h3 class="quote-modal-title"><i class="fa fa-file-invoice" style="color:var(--color-primary);"></i> Submit Quote Request</h3>
                            <button class="cart-drawer-close quote-modal-close" aria-label="Close Modal">&times;</button>
                        </div>
                        <div class="quote-modal-body">
                            <form id="rfq-checkout-form">
                                <input type="hidden" id="rfq-items-description" name="items_description">
                                
                                <div class="form-group">
                                    <label class="form-label" for="rfq-name">Your Name *</label>
                                    <input class="form-input" type="text" id="rfq-name" required placeholder="John Doe">
                                </div>
                                <div class="form-group">
                                    <label class="form-label" for="rfq-email">Business Email *</label>
                                    <input class="form-input" type="email" id="rfq-email" required placeholder="john@company.com">
                                </div>
                                <div class="form-group">
                                    <label class="form-label" for="rfq-phone">Phone Number *</label>
                                    <input class="form-input" type="tel" id="rfq-phone" required placeholder="+971 50 123 4567">
                                </div>
                                <div class="form-group">
                                    <label class="form-label" for="rfq-company">Company Name *</label>
                                    <input class="form-input" type="text" id="rfq-company" required placeholder="My Company LLC">
                                </div>
                                <div class="form-group">
                                    <label class="form-label" for="rfq-specs">Branding Specifications (Optional)</label>
                                    <textarea class="form-textarea" id="rfq-specs" style="height:80px;" placeholder="e.g. Logo placement, engraving on pens, embroidery in 2 colors..."></textarea>
                                </div>
                                <div class="form-group">
                                    <label class="form-label" for="rfq-logo">Logo File Reference Name (Optional)</label>
                                    <input class="form-input" type="text" id="rfq-logo" placeholder="logo_vector.ai">
                                </div>
                                
                                <button class="btn btn-primary" type="submit" style="width:100%; margin-top:10px;">Send RFQ Package</button>
                            </form>
                        </div>
                    </div>
                </div>
        """
    else:
        main_content_html = f"""
                <div class="service-detail-content">
                    {" " if not main_image_url else f'<img class="service-main-img" src="{main_image_url}" alt="{service_name}">' }
                    <h2 style="font-size:2rem; margin-top:20px; margin-bottom:15px;">Overview</h2>
                    {p_html}
                    
                    {gallery_html}
                </div>
        """

    body = f"""
    <!-- Page Header -->
    <section class="page-header">
        <div class="container">
            <h1 class="page-header-title">{service_name}</h1>
            {generate_breadcrumbs(service_name, relative_depth)}
        </div>
    </section>

    <!-- Content Detail -->
    <section class="section" style="background-color:#ffffff;">
        <div class="container">
            <div class="service-detail-grid">
                {main_content_html}
                
                <div class="sidebar">
                    <div class="sidebar-widget">
                        <h3 class="widget-title">Our Services</h3>
                        {sidebar_menu}
                    </div>
                    
                    <div class="sidebar-widget contact-widget">
                        <h3 class="widget-title">Get a Quote</h3>
                        <p style="color:rgba(255,255,255,0.7); margin-bottom:20px; font-size:0.9rem;">Need pricing or consultations for our {service_name} services? Contact our support desk.</p>
                        <a href="{root_prefix}contact/index.html" class="btn btn-primary" style="width:100%;">Contact Us</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    
    html = get_shared_header(title, desc, relative_depth) + body + get_shared_footer(relative_depth, include_ecommerce=is_gifts)
    with open(os.path.join(OUTPUT_DIR, subfolder_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Compiled {subfolder_path}/index.html")

# 6. COMPILE BLOG LISTING PAGE (blog/index.html)
def compile_blog():
    with open(os.path.join(PARSED_DIR, "blog_parsed.json"), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    title = data['title']
    desc = data['description']
    
    os.makedirs(os.path.join(OUTPUT_DIR, "blog"), exist_ok=True)
    
    body = f"""
    <!-- Page Header -->
    <section class="page-header">
        <div class="container">
            <h1 class="page-header-title">Our Blog & Articles</h1>
            {generate_breadcrumbs("Blog", 1)}
        </div>
    </section>

    <!-- Blog Grid -->
    <section class="section" style="background-color:#ffffff;">
        <div class="container">
            <div class="blog-grid">
                
                <!-- Blog 1 -->
                <div class="blog-card">
                    <div class="blog-img-wrap">
                        <img class="blog-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2022/02/Vehicle-Branding-in-Dubai-800x800.jpg")}" alt="Vehicle Branding">
                    </div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <span><i class="fa fa-calendar"></i> February 15, 2022</span>
                            <span><i class="fa fa-user"></i> Admin</span>
                        </div>
                        <h3 class="blog-title-card">Everything You Need to Know About Vehicle Branding in Dubai</h3>
                        <p class="blog-desc-card">Vehicle wraps provide a mobile billboard for your brand, carrying your marketing messages to thousands of potential customers daily across Dubai...</p>
                        <a href="{OUTPUT_DIR}\contact\index.html" class="service-card-link" style="color:var(--color-primary);">Get branding quote <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Blog 2 -->
                <div class="blog-card">
                    <div class="blog-img-wrap">
                        <img class="blog-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2021/02/digital-printing-vs-offset-printing-800x800.jpg")}" alt="Digital vs Offset">
                    </div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <span><i class="fa fa-calendar"></i> January 20, 2021</span>
                            <span><i class="fa fa-user"></i> Admin</span>
                        </div>
                        <h3 class="blog-title-card">Digital Printing vs Offset Printing: Which One is Better?</h3>
                        <p class="blog-desc-card">Choosing the right printing technology depends on order volume, material types, turnaround speed, and custom data requirements. We explain the core differences...</p>
                        <a href="{OUTPUT_DIR}\contact\index.html" class="service-card-link" style="color:var(--color-primary);">Get printing quote <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

                <!-- Blog 3 -->
                <div class="blog-card">
                    <div class="blog-img-wrap">
                        <img class="blog-img" src="{resolve_img("https://www.ashandsims.com/wp-content/uploads/2022/02/Signage-for-Business-800x800.jpg")}" alt="Signage for Business">
                    </div>
                    <div class="blog-content">
                        <div class="blog-meta">
                            <span><i class="fa fa-calendar"></i> March 10, 2022</span>
                            <span><i class="fa fa-user"></i> Admin</span>
                        </div>
                        <h3 class="blog-title-card">How Signage Transforms Footfalls for Local Businesses</h3>
                        <p class="blog-desc-card">Quality exterior signage acts as your primary visual identity, boosting walk-in leads and solidifying corporate brick-and-mortar presence...</p>
                        <a href="{OUTPUT_DIR}\contact\index.html" class="service-card-link" style="color:var(--color-primary);">Get signage quote <i class="fa fa-arrow-right"></i></a>
                    </div>
                </div>

            </div>
        </div>
    </section>
    """
    
    html = get_shared_header(title, desc, 1) + body + get_shared_footer(1)
    with open(os.path.join(OUTPUT_DIR, "blog/index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Compiled blog/index.html")

print("=== Starting Site Compilation ===")
compile_home()
compile_about()
compile_contact()
compile_clients()
compile_services_index()
compile_blog()

# Compile Sub-services Detail Pages
# 1. Vehicle Branding (relative depth 3)
compile_subservice(
    "vehicle_branding_parsed.json",
    "services/large-format-digital-printing/vehicle-branding",
    3,
    "Vehicle Branding",
    1,
    [
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Vehicle-Branding-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Vehicle-Branding-02.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Vehicle-Branding-03.jpg"
    ]
)

# 2. Large Format Digital Printing (relative depth 2)
compile_subservice(
    "large_format_digital_printing_parsed.json",
    "services/large-format-digital-printing",
    2,
    "Large Format Digital Printing",
    2,
    [
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Posters-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Posters-02.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Posters-03.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Floor-Stickers-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Floor-Stickers-02.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Flex-01.jpg"
    ]
)

# 3. Fabrication (relative depth 2)
compile_subservice(
    "fabrication_parsed.json",
    "services/fabrication",
    2,
    "Exhibition Stand & Fabrication",
    3,
    [
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Exhibition-Stands-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Exhibition-Stands-02.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Exhibition-Stands-03.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Kiosks-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Kiosks-02.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Retail-Pop-Up-Activation-01.jpg"
    ]
)

# 4. Flags / Fabric Printing (relative depth 2)
compile_subservice(
    "flags_fabric_printing_parsed.json",
    "services/flags-fabric-printing",
    2,
    "Flags & Fabric Printing",
    4,
    [
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Teardrop-Flags-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Teardrop-Flags-02.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Telescopic-Flags-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/H-Flags-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Tents.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Umbrellas.jpg"
    ]
)

# 5. Signage (relative depth 2)
compile_subservice(
    "signage_parsed.json",
    "services/signage",
    2,
    "Signage Manufacturing",
    5,
    [
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Signage-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Signage-02.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Signage-03.jpg"
    ]
)

# 6. Corporate Gifts (relative depth 2)
compile_subservice(
    "corporate_gifts_parsed.json",
    "services/corporate-gifts",
    2,
    "Corporate Gifts",
    6,
    [
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Pens-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Pens-02.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Caps-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/T-Shirts-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/USB-Drives-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Organizers-01.jpg"
    ]
)

# 7. Designing (relative depth 2)
compile_subservice(
    "designing_parsed.json",
    "services/designing",
    2,
    "Branding & Graphic Designing",
    7,
    [
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Designing-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Designing-02.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Designing-03.jpg"
    ]
)

# 8. Offset Printing (relative depth 2)
compile_subservice(
    "offset_printing_parsed.json",
    "services/offset-printing",
    2,
    "Offset Printing Services",
    8,
    [
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Business-Cards-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Business-Cards-02.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Letterheads-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Envelopes-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Notepads-01.jpg",
        "https://www.ashandsims.com/wp-content/uploads/2021/06/Flyers-01.jpg"
    ]
)

print("=== Site Compilation Completed ===")
