import { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import Card from '../components/Card';
import Loader from '../components/Loader';

export default function ReportsPage() {
  const [reports, setReports] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchReports = async () => {
      try {
        const res = await axios.get('/api/report');
        setReports(res.data.reports || []);
      } catch {
        setReports([]);
      } finally {
        setLoading(false);
      }
    };

    fetchReports();
  }, []);

  return (
    <>
      <Header />
      <main className="max-w-3xl mx-auto mt-10 p-4">
        <Card title="📄 Available Reports">
          {loading ? (
            <Loader />
          ) : reports.length === 0 ? (
            <p className="text-gray-500">No reports found.</p>
          ) : (
            <ul className="space-y-3">
              {reports.map((filename) => (
                <li key={filename} className="flex justify-between items-center bg-gray-50 p-3 rounded border">
                  <span className="font-mono text-sm">{filename}</span>
                  <a
                    href={`/api/report/${filename}`}
                    target="_blank"
                    className="text-indigo-600 underline text-sm"
                  >
                    Download
                  </a>
                </li>
              ))}
            </ul>
          )}
        </Card>
      </main>
    </>
  );
}

