export default function Login() {
  return (
    <div style={{ padding: '1rem' }}>
      <h2>Login</h2>
      <form>
        <input type="email" placeholder="Email" /><br/>
        <input type="password" placeholder="Senha" /><br/>
        <button type="submit">Entrar</button>
      </form>
    </div>
  );
}
