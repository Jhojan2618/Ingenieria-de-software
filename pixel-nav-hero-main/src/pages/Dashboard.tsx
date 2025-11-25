import { useState } from "react";
import {
  Home,
  LogOut,
  BarChart3,
  Trophy,
  Calendar,
  FileText,
  Bell,
  Settings,
} from "lucide-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";
import heroBg from "@/assets/hero-bg.png";
import logoControl from "@/assets/control_logo.png";

interface DashboardProps {
  username: string;
  onLogout: () => void;
}

const mockData = {
  gamesPlayed: 156,
  hoursPlayed: 342,
  achievementsUnlocked: 89,
  level: 42,
  weeklyActivity: [
    { day: "Lun", hours: 4 },
    { day: "Mar", hours: 6 },
    { day: "Mié", hours: 5 },
    { day: "Jue", hours: 8 },
    { day: "Vie", hours: 7 },
    { day: "Sáb", hours: 10 },
    { day: "Dom", hours: 9 },
  ],
  recentAchievements: [
    { name: "Maestro del Pixel", progress: 100 },
    { name: "Velocista Digital", progress: 75 },
    { name: "Coleccionista Pro", progress: 60 },
    { name: "Leyenda del Arcade", progress: 45 },
  ],
};

const AppSidebar = ({ onLogout }: { onLogout: () => void }) => {
  const [activeSection, setActiveSection] = useState("overview");
  const [isCollapsed, setIsCollapsed] = useState(false);

  const menuItems = [
    { id: "overview", title: "Overview", icon: Home },
    { id: "habits", title: "Registro de hábitos", icon: FileText },
    { id: "agenda", title: "Agenda y retos", icon: Calendar },
    { id: "metrics", title: "Métricas", icon: BarChart3 },
    { id: "survey", title: "Encuesta emocional", icon: Trophy },
    { id: "notifications", title: "Notificaciones", icon: Bell },
    { id: "settings", title: "Configuración", icon: Settings },
  ];

  return (
    <div
      className={`${isCollapsed ? "w-14" : "w-60"} bg-[#1a1a2e] flex flex-col h-screen border-r border-gray-700 transition-all duration-300`}
    >
      <div className="p-4 flex-1 flex flex-col">
        {/* Logo */}
        {!isCollapsed && (
          <div className="flex justify-center mb-8">
            <img src={logoControl} alt="Logo" className="h-12 w-12" />
          </div>
        )}

        {/* Menu */}
        <div className="flex-1">
          {!isCollapsed && (
            <h2 className="text-white font-bold text-sm mb-4">MENÚ PRINCIPAL</h2>
          )}

          <div className="space-y-2">
            {menuItems.map((item) => (
              <button
                key={item.id}
                onClick={() => setActiveSection(item.id)}
                className={`w-full flex items-center space-x-3 px-3 py-2 rounded-md text-left transition-colors ${
                  activeSection === item.id
                    ? "bg-yellow-400 text-black"
                    : "text-white hover:bg-blue-600/20"
                }`}
              >
                <item.icon className="h-4 w-4 flex-shrink-0" />
                {!isCollapsed && (
                  <span className="font-medium">{item.title}</span>
                )}
              </button>
            ))}
          </div>
        </div>

        {/* Logout */}
        <div className="mt-auto">
          <button
            onClick={onLogout}
            className="w-full flex items-center space-x-3 px-3 py-2 rounded-md text-red-400 hover:bg-red-500/20 transition-colors"
          >
            <LogOut className="h-4 w-4 flex-shrink-0" />
            {!isCollapsed && <span className="font-medium">Cerrar sesión</span>}
          </button>
        </div>
      </div>
    </div>
  );
};

export const Dashboard = ({ username, onLogout }: DashboardProps) => {
  return (
    <div
      className="min-h-screen flex w-full"
      style={{
        backgroundImage: `url(${heroBg})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        backgroundAttachment: "fixed",
      }}
    >
      <AppSidebar onLogout={onLogout} />

      <div className="flex-1 flex flex-col">
        {/* Header */}
        <header
          className="h-16 flex items-center border-b border-border px-6 gap-4"
          style={{ backgroundColor: "#26253D" }}
        >
          <div className="flex-1">
            <h1 className="text-2xl font-bold text-primary">
              ¡Hola, {username}!
            </h1>
          </div>
        </header>

        {/* Main Content */}
        <main className="flex-1 p-6 overflow-auto bg-transparent">
          <div className="max-w-7xl mx-auto space-y-6">
            {/* Stats Cards */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              {[
                { title: "JUEGOS JUGADOS", value: mockData.gamesPlayed },
                { title: "HORAS JUGADAS", value: `${mockData.hoursPlayed}h` },
                { title: "LOGROS", value: mockData.achievementsUnlocked },
                { title: "NIVEL", value: mockData.level },
              ].map((stat, i) => (
                <Card key={i} className="glass-effect pixel-border">
                  <CardHeader className="pb-3">
                    <CardTitle className="text-sm font-medium text-muted-foreground">
                      {stat.title}
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="text-3xl font-bold text-primary">
                      {stat.value}
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>

            {/* Charts Section */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Weekly Activity Chart */}
              <Card className="glass-effect pixel-border">
                <CardHeader>
                  <CardTitle className="text-primary">Actividad Semanal</CardTitle>
                  <CardDescription>Horas jugadas esta semana</CardDescription>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={250}>
                    <BarChart data={mockData.weeklyActivity}>
                      <CartesianGrid
                        strokeDasharray="3 3"
                        stroke="rgba(232, 180, 77, 0.1)"
                      />
                      <XAxis dataKey="day" stroke="hsl(var(--foreground))" />
                      <YAxis stroke="hsl(var(--foreground))" />
                      <Tooltip
                        contentStyle={{
                          backgroundColor: "rgba(38, 37, 61, 0.9)",
                          border: "2px solid rgba(232, 180, 77, 0.3)",
                          borderRadius: "4px",
                        }}
                      />
                      <Bar dataKey="hours" fill="hsl(var(--primary))" />
                    </BarChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>

              {/* Recent Achievements */}
              <Card className="glass-effect pixel-border">
                <CardHeader>
                  <CardTitle className="text-primary">Logros Recientes</CardTitle>
                  <CardDescription>
                    Tu progreso en los últimos logros
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  {mockData.recentAchievements.map((achievement, index) => (
                    <div key={index} className="space-y-2">
                      <div className="flex justify-between text-sm">
                        <span className="font-medium">{achievement.name}</span>
                        <span className="text-muted-foreground">
                          {achievement.progress}%
                        </span>
                      </div>
                      <Progress value={achievement.progress} className="h-2" />
                    </div>
                  ))}
                </CardContent>
              </Card>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
};
