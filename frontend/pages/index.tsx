import Link from 'next/link';
import Header from '../components/Header';
import Card from '../components/Card';

export default function Home() {
  return (
    <>
      <Header />
      <main className="min-h-screen bg-gray-100 py-16 px-4 flex items-center justify-center">
        <Card className="max-w-2xl text-center">
          <h1 className="text-3xl font-bold text-indigo-700 mb-4">🔐 RedCorps Sentinel</h1>
          <p className="text-gray-600 mb-6">
            AI-powered cybersecurity toolkit for fast, intelligent audits.<br />
            Scan, assess, and stay compliant — all in minutes.
          </p>
          <div className="flex justify-center gap-4">
            <Link href="/dashboard">
              <button className="bg-indigo-600 text-white px-5 py-2 rounded hover:bg-indigo-700">
                Go to Dashboard
              </button>
            </Link>
            <Link href="/reports">
              <button className="border border-indigo-600 text-indigo-600 px-5 py-2 rounded hover:bg-indigo-50">
                View Reports
              </button>
            </Link>
          </div>
        </Card>
      </main>
    </>
  );
}

