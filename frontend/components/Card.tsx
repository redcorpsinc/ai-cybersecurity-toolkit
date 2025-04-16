import { ReactNode } from 'react';

interface CardProps {
  title?: string;
  children: ReactNode;
  className?: string;
}

export default function Card({ title, children, className = '' }: CardProps) {
  return (
    <div className={`bg-white shadow-md rounded-lg p-5 ${className}`}>
      {title && <h3 className="text-lg font-semibold mb-3 text-indigo-700">{title}</h3>}
      {children}
    </div>
  );
}
