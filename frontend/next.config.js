/** @type {import('next').NextConfig} */
const nextConfig = {
  // appDir is now the default in Next.js 15+
  output: 'standalone',
  experimental: {
    outputFileTracingRoot: process.cwd(),
  },
}

module.exports = nextConfig 