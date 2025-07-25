import Header from '../components/Header';

export default function Home() {
  return (
    <div>
      <Header />
      <main style={{ padding: '1rem' }}>
        <h2>Bem-vindo ao Investimentos Avançados</h2>
        <p>Veja os melhores investimentos para o seu perfil.</p>
      </main>
    </div>
  );
}
