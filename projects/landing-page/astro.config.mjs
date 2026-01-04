// @ts-check
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	site: 'https://agentic-sdlc.dev',
	integrations: [sitemap()],
	vite: {
		css: {
			postcss: './postcss.config.mjs',
		},
	},
});
