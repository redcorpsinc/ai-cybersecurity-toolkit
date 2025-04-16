import { useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import Card from '../components/Card';
import Loader from '../components/Loader';

export default function ScanPage() {
  const [target, setTarget] = useState('');
  const [framework, setFramework] = useState('NIST CSF');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const res = await axios.post('/api/scan', { target, framework });
      setResult(res.data);
    } catch {
      setResult({ error: 'Scan failed or API not reachable.' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Header />
      <main className="max-w-2xl mx-auto mt-10 p-4">
        <Card title="🔍 Run New Scan">
          <form onSubmit={handleSubmit} className="space-y-4">
            <input
              type="text"
              placeholder="example.com"
              value={target}
              onChange={(e) => setTarget(e.target.value)}
              className="w-full p-2 border rounded"
              required
            />
            <select
              value={framework}
              onChange={(e) => setFramework(e.target.value)}
              className="w-full p-2 border rounded"
            >
              <option value="NIST CSF">NIST CSF</option>
              <option value="CIS v8">CIS Controls</option>
              <option value="PCI DSS">PCI DSS</option>
              <option value="ISO 27001">ISO 27001</option>
            </select>
            <button
              type="submit"
              className="bg-indigo-600 text-white px-4 py-2 rounded w-full"
            >
              {loading ? 'Scanning...' : 'Start Scan'}
            </button>
          </form>
        </Card>

        {loading && <Loader />}

        {result && !loading && (
          <Card title="📊 Scan Result" className="mt-6">
            {result.error ? (
              <p className="text-red-600">{result.error}</p>
            ) : (
              <>
                <p><strong>Target:</strong> {result.target}</p>
                <p><strong>Risk Score:</strong> {result.risk_score}</p>
                <p><strong>Summary:</strong> {result.summary}</p>
                <a
                  href={result.report_path}
                  className="text-blue-600 underline mt-2 inline-block"
                  target="_blank"
                >
                  View Full Report →
                </a>
              </>
            )}
          </Card>
        )}
      </main>
    </>
  );
}

