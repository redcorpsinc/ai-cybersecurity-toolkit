import Link from 'next/link';
import Header from '../components/Header';
import Card from '../components/Card';

export default function Dashboard() {
  return (
    <>
      <Header />
      <main className="max-w-5xl mx-auto py-12 px-4">
        <h1 className="text-3xl font-bold text-indigo-700 mb-6">📊 Dashboard</h1>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Card title="Run a New Scan">
            <p className="text-sm text-gray-500 mb-4">
              Launch a fresh security audit using AI-based assessment.
            </p>
            <Link href="/scan">
              <button className="bg-indigo-600 text-white px-4 py-2 rounded">
                Launch Scan
              </button>
            </Link>
          </Card>

          <Card title="View Previous Reports">
            <p className="text-sm text-gray-500 mb-4">
              Browse and download completed PDF audit reports.
            </p>
            <Link href="/reports">
              <button className="border border-indigo-600 text-indigo-600 px-4 py-2 rounded">
                View Reports
              </button>
            </Link>
          </Card>
        </div>
      </main>
    </>
  );
}

