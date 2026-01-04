/** @type {import('tailwindcss').Config} */
export default {
    content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                // shadcn-inspired color system
                background: 'hsl(222.2 84% 4.9%)',
                foreground: 'hsl(210 40% 98%)',
                card: 'hsl(222.2 84% 4.9%)',
                'card-foreground': 'hsl(210 40% 98%)',
                primary: 'hsl(217.2 91.2% 59.8%)',
                'primary-foreground': 'hsl(222.2 47.4% 11.2%)',
                secondary: 'hsl(217.2 32.6% 17.5%)',
                'secondary-foreground': 'hsl(210 40% 98%)',
                muted: 'hsl(217.2 32.6% 17.5%)',
                'muted-foreground': 'hsl(215 20.2% 65.1%)',
                accent: 'hsl(217.2 32.6% 17.5%)',
                'accent-foreground': 'hsl(210 40% 98%)',
                border: 'hsl(217.2 32.6% 17.5%)',
                ring: 'hsl(224.3 76.3% 48%)',
            },
            fontFamily: {
                sans: ['Inter', 'system-ui', 'sans-serif'],
            },
            animation: {
                'fade-in': 'fadeIn 0.5s ease-out',
                'slide-up': 'slideUp 0.5s ease-out',
                'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
            },
            keyframes: {
                fadeIn: {
                    '0%': { opacity: '0' },
                    '100%': { opacity: '1' },
                },
                slideUp: {
                    '0%': { opacity: '0', transform: 'translateY(20px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                },
            },
        },
    },
    plugins: [],
};
