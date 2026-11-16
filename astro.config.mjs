import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import vercel from '@astrojs/vercel';

export default defineConfig({
  adapter: vercel(),

  image: {
    domains: ['fiorefoodscanada.com']
  },

  vite: {
    plugins: [tailwindcss()]
  }
});