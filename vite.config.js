import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        about: resolve(__dirname, 'about/index.html'),
        services: resolve(__dirname, 'services/index.html'),
        vehicle_branding: resolve(__dirname, 'services/large-format-digital-printing/vehicle-branding/index.html'),
        large_format_digital_printing: resolve(__dirname, 'services/large-format-digital-printing/index.html'),
        fabrication: resolve(__dirname, 'services/fabrication/index.html'),
        flags_fabric_printing: resolve(__dirname, 'services/flags-fabric-printing/index.html'),
        signage: resolve(__dirname, 'services/signage/index.html'),
        corporate_gifts: resolve(__dirname, 'services/corporate-gifts/index.html'),
        designing: resolve(__dirname, 'services/designing/index.html'),
        offset_printing: resolve(__dirname, 'services/offset-printing/index.html'),
        clients: resolve(__dirname, 'clients/index.html'),
        blog: resolve(__dirname, 'blog/index.html'),
        contact: resolve(__dirname, 'contact/index.html')
      }
    }
  }
});
