interface ContentSectionProps {
  id: string;
  title: string;
  children: React.ReactNode;
}

export const ContentSection = ({ id, title, children }: ContentSectionProps) => {
  return (
    <section id={id} className="min-h-screen py-20 px-4 sm:px-6 lg:px-8">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-4xl md:text-5xl font-bold text-primary mb-8 text-center pixel-border inline-block px-4 py-2">
          {title}
        </h2>
        <div className="glass-effect rounded-lg p-8 pixel-border">
          {children}
        </div>
      </div>
    </section>
  );
};
