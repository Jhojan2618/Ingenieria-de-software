import logoCen from "@/assets/beemo.png";
import { Button } from "@/components/ui/button";
import { Play, BarChart3, Shield, Clock, Bell, Settings } from "lucide-react";

export const HeroSection = () => {
  return (
    <section
      id="home"
      className="min-h-screen flex items-center justify-center relative overflow-hidden"
    >
      {/* Contenido principal */}
      <div className="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="space-y-12">
          
          {/* Título y botones - lado izquierdo */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
            <div className="glass-effect p-8 rounded-lg bg-black/20 backdrop-blur-sm animate-fade-in">
              <div className="space-y-8">
                {/* Título principal */}
                <div className="space-y-4">
                  <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-foreground leading-tight">
                    Equilibrio entre estudio y videojuegos
                  </h1>
                  <p className="text-xl text-muted-foreground leading-relaxed">
                    Monitorea hábitos, recibe alertas y mejora el bienestar emocional.
                  </p>
                </div>

                {/* Botones principales */}
                <div className="flex flex-col sm:flex-row gap-4">
                  <Button 
                    size="lg" 
                    className="pixel-border bg-orange-500 hover:bg-orange-600 text-white text-lg px-8 py-4"
                  >
                    <Play className="mr-2" size={20} />
                    Comenzar
                  </Button>
                  <Button 
                    size="lg" 
                    variant="outline" 
                    className="pixel-border bg-green-500 hover:bg-green-600 text-white text-lg px-8 py-4"
                  >
                    Ver demo
                  </Button>
                </div>
              </div>
            </div>

            {/* Lado derecho - Logo central */}
            <div className="flex justify-center lg:justify-end items-start">
              <div className="relative -mt-8">
                <img
                  src={logoCen}
                  alt="Teen Gaming Hub"
                  className="w-96 h-96 md:w-[28rem] md:h-[28rem] object-contain hover-scale"
                />
              </div>
            </div>
          </div>

          {/* Características principales - ancho completo */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full">
            <div className="glass-effect p-6 rounded-lg h-24 flex items-center">
              <div className="flex items-center space-x-3">
                <Bell className="text-primary flex-shrink-0" size={24} />
                <div className="space-y-1">
                  <p className="font-semibold text-sm text-foreground">Alertas inteligentes</p>
                  <p className="font-semibold text-xs text-muted-foreground">Notificaciones personalizadas</p>
                </div>
              </div>
            </div>

            <div className="glass-effect p-6 rounded-lg h-24 flex items-center">
              <div className="flex items-center space-x-3">
                <BarChart3 className="text-primary flex-shrink-0" size={24} />
                <div className="space-y-1">
                  <p className="font-semibold text-sm text-foreground">Métricas claras</p>
                  <p className="font-semibold text-xs text-muted-foreground">Gráficos semanales/mensuales</p>
                </div>
              </div>
            </div>

            <div className="glass-effect p-6 rounded-lg h-24 flex items-center">
              <div className="flex items-center space-x-3">
                <Shield className="text-primary flex-shrink-0" size={24} />
                <div className="space-y-1">
                  <p className="font-semibold text-sm text-foreground">Control parental</p>
                  <p className="font-semibold text-xs text-muted-foreground">Límites de tiempo y horarios</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Texto decorativo de fondo */}
      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 opacity-10">
        <div className="text-center">
          <h2 className="text-6xl md:text-8xl font-bold text-foreground">TEEN HEALTH</h2>
          <h2 className="text-6xl md:text-8xl font-bold text-primary">& GAMING</h2>
        </div>
      </div>
    </section>
  );
};
