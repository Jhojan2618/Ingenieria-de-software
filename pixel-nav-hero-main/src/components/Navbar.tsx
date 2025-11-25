import { useState } from "react";
import { Menu, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import logoControl from "@/assets/control_logo.png";

interface NavbarProps {
  onLoginClick: () => void;
}

export const Navbar = ({ onLoginClick }: NavbarProps) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
      setIsMenuOpen(false);
    }
  };

  const handleLogoClick = () => {
    // Reinicia la página al hacer scroll al inicio
    window.scrollTo({ top: 0, behavior: "smooth" });
    setIsMenuOpen(false);
  };

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 pixel-border" style={{ backgroundColor: '#26253D' }}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo y navegación del lado izquierdo */}
          <div className="flex items-center space-x-8">
            {/* Logo con funcionalidad de reinicio */}
            <button onClick={handleLogoClick} className="flex-shrink-0 hover:opacity-80 transition-opacity">
              <img src={logoControl} alt="Logo" className="h-12 w-12" />
            </button>

            {/* Desktop Navigation */}
            <div className="hidden md:flex items-center space-x-6">
              <button
                onClick={() => scrollToSection("home")}
                className="text-foreground hover:text-primary transition-colors font-medium"
              >
                HOME
              </button>
              <button
                onClick={() => scrollToSection("community")}
                className="text-foreground hover:text-primary transition-colors font-medium"
              >
                COMMUNITY
              </button>
              <button
                onClick={() => scrollToSection("contact")}
                className="text-foreground hover:text-primary transition-colors font-medium"
              >
                CONTACT
              </button>
              <button
                onClick={() => scrollToSection("about")}
                className="text-foreground hover:text-primary transition-colors font-medium"
              >
                ABOUT
              </button>
            </div>
          </div>

          {/* Lado derecho - Login y menú móvil */}
          <div className="flex items-center space-x-4">
            {/* Botón de login - solo visible en desktop */}
            <div className="hidden md:block">
              <Button
                onClick={onLoginClick}
                className="pixel-border bg-primary text-primary-foreground hover:bg-primary/90"
              >
                LOGIN
              </Button>
            </div>

            {/* Mobile menu button */}
            <div className="md:hidden">
              <button
                onClick={() => setIsMenuOpen(!isMenuOpen)}
                className="text-foreground hover:text-primary"
              >
                {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Mobile Navigation */}
      {isMenuOpen && (
        <div className="md:hidden glass-effect">
          <div className="px-2 pt-2 pb-3 space-y-1">
            <button
              onClick={() => scrollToSection("home")}
              className="block w-full text-left px-3 py-2 text-foreground hover:text-primary hover:bg-secondary/50 transition-colors font-medium"
            >
              HOME
            </button>
            <button
              onClick={() => scrollToSection("community")}
              className="block w-full text-left px-3 py-2 text-foreground hover:text-primary hover:bg-secondary/50 transition-colors font-medium"
            >
              COMMUNITY
            </button>
            <button
              onClick={() => scrollToSection("contact")}
              className="block w-full text-left px-3 py-2 text-foreground hover:text-primary hover:bg-secondary/50 transition-colors font-medium"
            >
              CONTACT
            </button>
            <button
              onClick={() => scrollToSection("about")}
              className="block w-full text-left px-3 py-2 text-foreground hover:text-primary hover:bg-secondary/50 transition-colors font-medium"
            >
              ABOUT
            </button>
            <div className="px-3 pt-2">
              <Button
                onClick={onLoginClick}
                className="w-full pixel-border bg-primary text-primary-foreground hover:bg-primary/90"
              >
                LOGIN
              </Button>
            </div>
          </div>
        </div>
      )}
    </nav>
  );
};
