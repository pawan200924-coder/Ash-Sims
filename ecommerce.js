// B2B Corporate Gifts E-Commerce State Management

const PRODUCTS = [
  {
    id: 'metal-pen-01',
    name: 'Premium Metal Pen',
    category: 'writing',
    desc: 'Elegant brushed aluminum ballpoint pen with chrome accents. Perfect for corporate engraving.',
    basePrice: 4.50,
    minQty: 200,
    image: '/assets/images/Pens-01.jpg',
    badge: 'Best Seller'
  },
  {
    id: 'exec-pen-02',
    name: 'Executive Ballpoint Pen',
    category: 'writing',
    desc: 'Heavyweight lacquer finish metal pen with smooth ink flow. Comes with executive presentation gift box.',
    basePrice: 6.80,
    minQty: 100,
    image: '/assets/images/Pens-02.jpg',
    badge: 'Premium'
  },
  {
    id: 'stylus-pen-03',
    name: 'Custom Stylus Pen',
    category: 'writing',
    desc: 'Dual-function twist action pen with soft rubber stylus tip for tablets and touchscreens.',
    basePrice: 2.20,
    minQty: 500,
    image: '/assets/images/Pens-03.jpg',
    badge: 'Popular'
  },
  {
    id: 'cotton-cap-01',
    name: 'Premium Cotton Cap',
    category: 'apparel',
    desc: '100% brushed cotton 6-panel cap with adjustable brass buckle. Excellent area for logo embroidery.',
    basePrice: 9.50,
    minQty: 100,
    image: '/assets/images/Caps-01.jpg',
    badge: 'Hot'
  },
  {
    id: 'mesh-cap-02',
    name: 'Outdoor Trucker Cap',
    category: 'apparel',
    desc: 'Lightweight structured cap with breathable mesh back. Ideal for company team building events.',
    basePrice: 8.00,
    minQty: 100,
    image: '/assets/images/Caps-02.jpg',
    badge: 'Eco'
  },
  {
    id: 'visual-cap-03',
    name: 'Sporty Visor Cap',
    category: 'apparel',
    desc: 'Low profile sports visor cap with moisture-wicking sweatband. Perfect for branding.',
    basePrice: 10.50,
    minQty: 100,
    image: '/assets/images/Caps-03.jpg',
    badge: 'New'
  },
  {
    id: 'polo-shirt-01',
    name: 'Corporate Polo Shirt',
    category: 'apparel',
    desc: 'Pique knit cotton-poly blend polo shirt. Breathable, anti-pill fabric, customized logo chest embroidery.',
    basePrice: 26.00,
    minQty: 50,
    image: '/assets/images/Shirts-01.jpg',
    badge: 'Executive'
  },
  {
    id: 'tshirt-promo-01',
    name: 'Promo Crewneck T-Shirt',
    category: 'apparel',
    desc: 'Comfortable 180GSM combed cotton crewneck t-shirt. Ideal for mass promotional giveaways.',
    basePrice: 14.00,
    minQty: 100,
    image: '/assets/images/T-Shirts-01.jpg',
    badge: 'Bulk Value'
  },
  {
    id: 'tshirt-fit-02',
    name: 'Premium Fitted T-Shirt',
    category: 'apparel',
    desc: 'Soft cotton crewneck shirt with tailored fit. Perfect for corporate uniform branding.',
    basePrice: 16.50,
    minQty: 100,
    image: '/assets/images/T-Shirts-02.jpg',
    badge: 'Retail Quality'
  },
  {
    id: 'leather-journal-01',
    name: 'Leatherette Journal Organizer',
    category: 'stationery',
    desc: 'Soft-touch PU leather notebook with bookmark ribbon and elastic closure band. Debossed branding options.',
    basePrice: 18.00,
    minQty: 50,
    image: '/assets/images/Organizers-01.jpg',
    badge: 'Corporate Favourite'
  },
  {
    id: 'portfolio-zip-02',
    name: 'Executive Portfolio Organizer',
    category: 'stationery',
    desc: 'Deluxe zippered portfolio padfolio containing document pockets, pen loops, and A4 writing pad.',
    basePrice: 28.00,
    minQty: 50,
    image: '/assets/images/Organizers-02.jpg',
    badge: 'VIP Gift'
  },
  {
    id: 'passport-holder-01',
    name: 'Leather Passport Holder',
    category: 'stationery',
    desc: 'Premium split-leather travel passport holder with credit card slots and boarding pass flap.',
    basePrice: 15.00,
    minQty: 100,
    image: '/assets/images/Passport-Holders.jpg',
    badge: 'Travel Classic'
  },
  {
    id: 'swivel-usb-01',
    name: 'Swivel Metal USB Drive',
    category: 'tech',
    desc: 'Classic swivel metal shell USB 3.0 flash drive. Includes dual-sided screen print or laser engraving.',
    basePrice: 11.00,
    minQty: 100,
    image: '/assets/images/USB-Drives-01.jpg',
    badge: 'Office Essential'
  },
  {
    id: 'card-usb-02',
    name: 'Credit Card Style USB Drive',
    category: 'tech',
    desc: 'Ultra-thin card format USB. Offers a full-bleed double-sided photographic print area.',
    basePrice: 12.50,
    minQty: 100,
    image: '/assets/images/USB-Drives-02.jpg',
    badge: 'Slim Fit'
  },
  {
    id: 'key-usb-03',
    name: 'Executive Key USB Drive',
    category: 'tech',
    desc: 'Sleek key-shaped metal design that clips onto keyrings. Highly durable and premium look.',
    basePrice: 14.50,
    minQty: 100,
    image: '/assets/images/USB-Drives-03.jpg',
    badge: 'VIP Tech'
  }
];

let cart = JSON.parse(localStorage.getItem('gift_cart')) || [];

// Calculate unit price based on volume quantity discounts
function getUnitPrice(basePrice, qty) {
  if (qty >= 1000) return basePrice * 0.75; // 25% discount
  if (qty >= 500) return basePrice * 0.82;  // 18% discount
  if (qty >= 250) return basePrice * 0.90;  // 10% discount
  return basePrice;
}

// Render product catalog cards
function renderCatalog(filter = 'all') {
  const grid = document.querySelector('.products-grid');
  if (!grid) return;
  
  grid.innerHTML = '';
  
  const filteredProducts = filter === 'all' 
    ? PRODUCTS 
    : PRODUCTS.filter(p => p.category === filter);
    
  filteredProducts.forEach(p => {
    const card = document.createElement('div');
    card.className = 'product-card';
    
    const badgeHtml = p.badge ? `<div class="product-badge">${p.badge}</div>` : '';
    
    card.innerHTML = `
      <div class="product-img-wrap">
        ${badgeHtml}
        <img class="product-img" src="${p.image}" alt="${p.name}">
      </div>
      <div class="product-content">
        <h3 class="product-title">${p.name}</h3>
        <p class="product-desc">${p.desc}</p>
        <div class="product-price-info">
          <span class="product-price">AED ${p.basePrice.toFixed(2)}</span>
          <span class="product-price-unit">/ unit (Min. ${p.minQty} units)</span>
        </div>
        <button class="btn btn-primary product-btn" data-id="${p.id}">
          <i class="fa fa-shopping-basket"></i> Add to Quote
        </button>
      </div>
    `;
    
    // Bind click event
    card.querySelector('.product-btn').addEventListener('click', () => {
      addToCart(p.id);
    });
    
    grid.appendChild(card);
  });
}

// Setup filter tabs
function setupFilters() {
  const container = document.querySelector('.catalog-filters');
  if (!container) return;
  
  const categories = [
    { label: 'All Products', id: 'all' },
    { label: 'Writing Instruments', id: 'writing' },
    { label: 'Apparel Uniforms', id: 'apparel' },
    { label: 'Office Stationery', id: 'stationery' },
    { label: 'Tech Gadgets', id: 'tech' }
  ];
  
  container.innerHTML = '';
  
  categories.forEach((cat, index) => {
    const btn = document.createElement('button');
    btn.className = `filter-btn ${index === 0 ? 'active' : ''}`;
    btn.textContent = cat.label;
    btn.setAttribute('data-id', cat.id);
    
    btn.addEventListener('click', (e) => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderCatalog(cat.id);
    });
    
    container.appendChild(btn);
  });
}

// Update local storage and update header/drawer UI
function saveCart() {
  localStorage.setItem('gift_cart', JSON.stringify(cart));
  updateCartUI();
}

// Add item to cart
function addToCart(productId) {
  const product = PRODUCTS.find(p => p.id === productId);
  if (!product) return;
  
  const existingItem = cart.find(item => item.id === productId);
  if (existingItem) {
    existingItem.qty += 50; // increment in packages of 50
  } else {
    cart.push({
      id: product.id,
      name: product.name,
      basePrice: product.basePrice,
      qty: product.minQty,
      image: product.image,
      minQty: product.minQty
    });
  }
  
  saveCart();
  openCartDrawer();
}

// Remove item from cart
function removeFromCart(productId) {
  cart = cart.filter(item => item.id !== productId);
  saveCart();
}

// Update quantity
function updateQuantity(productId, newQty) {
  const item = cart.find(item => item.id === productId);
  if (!item) return;
  
  const qty = parseInt(newQty);
  if (isNaN(qty) || qty < item.minQty) {
    item.qty = item.minQty; // reset to MOQ if invalid
  } else {
    item.qty = qty;
  }
  saveCart();
}

// Open / Close Cart Drawers
function openCartDrawer() {
  const drawer = document.querySelector('.cart-drawer');
  const backdrop = document.querySelector('.cart-drawer-backdrop');
  if (drawer && backdrop) {
    drawer.classList.add('open');
    backdrop.classList.add('open');
  }
}

function closeCartDrawer() {
  const drawer = document.querySelector('.cart-drawer');
  const backdrop = document.querySelector('.cart-drawer-backdrop');
  if (drawer && backdrop) {
    drawer.classList.remove('open');
    backdrop.classList.remove('open');
  }
}

// Render dynamic cart contents
function updateCartUI() {
  // Update floating button count
  const badgeCount = document.querySelector('.cart-badge-count');
  if (badgeCount) {
    const totalItems = cart.reduce((sum, item) => sum + 1, 0); // count distinct products
    badgeCount.textContent = totalItems;
    badgeCount.style.display = totalItems > 0 ? 'flex' : 'none';
  }
  
  // Render sidebar contents
  const body = document.querySelector('.cart-drawer-body');
  if (!body) return;
  
  body.innerHTML = '';
  
  if (cart.length === 0) {
    body.innerHTML = `
      <div class="cart-empty-message">
        <i class="fa fa-shopping-basket"></i>
        <p>Your quote cart is empty.</p>
        <p style="font-size:0.8rem; margin-top:8px;">Browse our catalog and add promotional gifts to request pricing.</p>
      </div>
    `;
    
    // Disable quote button
    const submitBtn = document.querySelector('.cart-checkout-btn');
    if (submitBtn) submitBtn.disabled = true;
    
    // Hide footer values
    document.querySelector('.cart-summary-subtotal-val').textContent = 'AED 0.00';
    document.querySelector('.cart-summary-discount-val').textContent = '0%';
    document.querySelector('.cart-summary-total-val').textContent = 'AED 0.00';
    return;
  }
  
  let subtotal = 0;
  let totalDiscounted = 0;
  
  cart.forEach(item => {
    const unitPrice = getUnitPrice(item.basePrice, item.qty);
    const itemTotal = unitPrice * item.qty;
    subtotal += item.basePrice * item.qty;
    totalDiscounted += itemTotal;
    
    const discPercentage = Math.round((1 - (unitPrice / item.basePrice)) * 100);
    const badgeDisc = discPercentage > 0 ? `<span style="background:#25d366; color:#fff; padding:2px 6px; border-radius:10px; font-size:0.7rem; font-weight:600; margin-left:8px;">-${discPercentage}% Bulk Disc.</span>` : '';
    
    const cartItemDiv = document.createElement('div');
    cartItemDiv.className = 'cart-item';
    
    cartItemDiv.innerHTML = `
      <img class="cart-item-img" src="${item.image}" alt="${item.name}">
      <div class="cart-item-info">
        <h4 class="cart-item-title">${item.name}</h4>
        <div class="cart-item-qty-wrap">
          <label style="font-size:0.75rem; color:var(--color-text-muted);">Quantity:</label>
          <input class="cart-item-qty-input" type="number" min="${item.minQty}" step="50" value="${item.qty}" data-id="${item.id}">
        </div>
        <div class="cart-item-price-info">
          <span style="color:var(--color-text-muted);">AED ${unitPrice.toFixed(2)}/unit</span>
          ${badgeDisc}
        </div>
        <div style="margin-top:6px; font-size:0.9rem;">
          Subtotal: <span class="cart-item-total">AED ${itemTotal.toFixed(2)}</span>
        </div>
      </div>
      <button class="cart-item-remove" data-id="${item.id}"><i class="fa fa-trash-alt"></i></button>
    `;
    
    // Bind quantity change event
    cartItemDiv.querySelector('.cart-item-qty-input').addEventListener('change', (e) => {
      updateQuantity(item.id, e.target.value);
    });
    
    // Bind remove event
    cartItemDiv.querySelector('.cart-item-remove').addEventListener('click', () => {
      removeFromCart(item.id);
    });
    
    body.appendChild(cartItemDiv);
  });
  
  // Enable submit quote button
  const submitBtn = document.querySelector('.cart-checkout-btn');
  if (submitBtn) submitBtn.disabled = false;
  
  const avgDiscount = Math.round((1 - (totalDiscounted / subtotal)) * 100);
  
  document.querySelector('.cart-summary-subtotal-val').textContent = `AED ${subtotal.toFixed(2)}`;
  document.querySelector('.cart-summary-discount-val').textContent = `${avgDiscount}%`;
  document.querySelector('.cart-summary-total-val').textContent = `AED ${totalDiscounted.toFixed(2)}`;
}

// Open checkout RFQ modal dialog
function openRFQModal() {
  const backdrop = document.querySelector('.quote-modal-backdrop');
  if (!backdrop) return;
  
  backdrop.classList.add('open');
  closeCartDrawer();
  
  // Populate hidden selected items description
  const descField = document.getElementById('rfq-items-description');
  if (descField) {
    const list = cart.map(item => `- ${item.name} (${item.qty} units @ AED ${getUnitPrice(item.basePrice, item.qty).toFixed(2)}/unit)`).join('\n');
    descField.value = list;
  }
}

function closeRFQModal() {
  const backdrop = document.querySelector('.quote-modal-backdrop');
  if (backdrop) {
    backdrop.classList.remove('open');
  }
}

// Initialise ecommerce triggers on document load
document.addEventListener('DOMContentLoaded', () => {
  setupFilters();
  renderCatalog('all');
  updateCartUI();
  
  // Event listeners for Cart Drawer
  const floatBtn = document.querySelector('.cart-float-btn');
  if (floatBtn) {
    floatBtn.addEventListener('click', openCartDrawer);
  }
  
  const closeBtn = document.querySelector('.cart-drawer-close');
  if (closeBtn) {
    closeBtn.addEventListener('click', closeCartDrawer);
  }
  
  const backdrop = document.querySelector('.cart-drawer-backdrop');
  if (backdrop) {
    backdrop.addEventListener('click', closeCartDrawer);
  }
  
  const rfqCheckoutBtn = document.querySelector('.cart-checkout-btn');
  if (rfqCheckoutBtn) {
    rfqCheckoutBtn.addEventListener('click', openRFQModal);
  }
  
  // Event listeners for Quote Modal
  const closeQuoteBtn = document.querySelector('.quote-modal-close');
  if (closeQuoteBtn) {
    closeQuoteBtn.addEventListener('click', closeRFQModal);
  }
  
  const quoteBackdrop = document.querySelector('.quote-modal-backdrop');
  if (quoteBackdrop) {
    quoteBackdrop.addEventListener('click', (e) => {
      if (e.target === quoteBackdrop) {
        closeRFQModal();
      }
    });
  }
  
  const rfqForm = document.getElementById('rfq-checkout-form');
  if (rfqForm) {
    rfqForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const submitBtn = rfqForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = 'Opening WhatsApp...';
      
      const name = document.getElementById('rfq-name').value;
      const email = document.getElementById('rfq-email').value;
      const phone = document.getElementById('rfq-phone').value;
      const company = document.getElementById('rfq-company').value;
      const specs = document.getElementById('rfq-specs').value || 'None';
      const logo = document.getElementById('rfq-logo').value || 'None';

      let itemsText = cart.map(item => {
        const unitPrice = getUnitPrice(item.basePrice, item.qty);
        const total = unitPrice * item.qty;
        return `• ${item.name} (${item.qty} units @ AED ${unitPrice.toFixed(2)}/unit = AED ${total.toFixed(2)})`;
      }).join('\n');

      let totalEstimate = cart.reduce((sum, item) => sum + (getUnitPrice(item.basePrice, item.qty) * item.qty), 0);

      const rfqMessage = `*New B2B Quote Request - Ash & Sims Website*\n\n` +
                         `*Company Name:* ${company}\n` +
                         `*Contact Name:* ${name}\n` +
                         `*Business Email:* ${email}\n` +
                         `*Phone Number:* ${phone}\n\n` +
                         `*Selected Items:*\n${itemsText}\n\n` +
                         `*Estimated Total:* AED ${totalEstimate.toFixed(2)}\n\n` +
                         `*Branding Specs:* ${specs}\n` +
                         `*Logo Reference:* ${logo}`;

      const waUrl = `https://wa.me/971554151136?text=${encodeURIComponent(rfqMessage)}`;
      
      setTimeout(() => {
        window.open(waUrl, '_blank');
        cart = [];
        saveCart();
        closeRFQModal();
        rfqForm.reset();
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
      }, 800);
    });
  }
});
