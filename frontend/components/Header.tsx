import Link from 'next/link';

export default function Header() {
  return (
    <header className="bg-indigo-700 text-white p-4 shadow">
      <div className="max-w-6xl mx-auto flex justify-between items-center">
        <Link href="/">
          <span className="text-xl font-bold cursor-pointer">🔐 RedCorps Sentinel</span>
        </Link>
        <nav className="space-x-4 text-sm">
          <Link href="/dashboard" className="hover:underline">
            Dashboard
          </Link>
          <Link href="/scan" className="hover:underline">
            Scan
          </Link>
          <Link href="/reports" className="hover:underline">
            Reports
          </Link>
        </nav>
      </div>
    </header>
  );
}
