import TypingTest from '@/components/TypingTest';
import ThemeToggle from '@/components/ThemeToggle';

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-8">
      <header className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold">Key Blaze</h1>
        <ThemeToggle />
      </header>
      <main>
        <TypingTest />
      </main>
      <footer className="bg-gray-900 text-white py-8 text-center">
  <div className="container mx-auto">
    <p className="text-sm md:text-base font-light">
      Made with{' '}
      <span className="text-red-500 animate-pulse">❤</span> by{' '}
      <a
        href="https://github.com/kekubhai"
        target="_blank"
        rel="noopener noreferrer"
        className="text-purple-400 hover:text-purple-500 underline transition-all duration-300 ease-in-out"
      >
        Anirban Ghosh
      </a>
    </p>
    <div className="mt-4">
     
    </div>
  </div>
</footer>

    </div>
  )
}
