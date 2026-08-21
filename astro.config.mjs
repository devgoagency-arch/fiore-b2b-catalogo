import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  image: {
    domains: ['fiorefoodscanada.com']
  },

  vite: {
    plugins: [tailwindcss()]
  }
});