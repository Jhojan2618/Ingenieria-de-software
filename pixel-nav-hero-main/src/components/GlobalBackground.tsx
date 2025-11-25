import fondoLogo from "@/assets/fondo_logo.png";

export const GlobalBackground = () => {
  return (
    <div 
      className="fixed inset-0 z-0 pointer-events-none"
      style={{
        backgroundImage: `url(${fondoLogo})`,
        backgroundSize: "contain",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        opacity: 0.15, // Más transparente
        filter: "blur(1px)", // Con un poco de desenfoque
      }}
    />
  );
};
