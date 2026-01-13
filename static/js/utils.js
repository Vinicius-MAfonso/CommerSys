const fillFields = (data, mapping) => {
  Object.entries(mapping).forEach(([htmlId, apiKey]) => {
    const element = document.getElementById(htmlId);
    if (element) element.value = data[apiKey] || "";
  });
};

const btn_cnpj = document.getElementById("btnCnpj");
if (btn_cnpj) {
  btn_cnpj.addEventListener("click", async () => {
    const input = document.querySelector("#id_cpf_cnpj, #id_cnpj");
    const cnpjLimpo = input.value.replace(/\D/g, "");

    if (cnpjLimpo.length !== 14) return alert("CNPJ Inválido");

    try {
      btn_cnpj.disabled = true; 
      const response = await fetch(`https://brasilapi.com.br/api/cnpj/v1/${cnpjLimpo}`);
      
      if (!response.ok) throw new Error("CNPJ não encontrado");

      const data = await response.json();
      fillFields(data, {
        id_nome_razao_social: "razao_social",
        id_telefone: "ddd_telefone_1",
        id_email: "email",
        id_cep: "cep",
      });
    } catch (error) {
      alert("Erro ao buscar CNPJ, tente mais tarde.");
      console.log(error.message);
    } finally {
      btn_cnpj.disabled = false;
    }
  });
}

const btn_cep = document.getElementById("btnCep");
if (btn_cep) {
  btn_cep.addEventListener("click", async () => {
    const input = document.getElementById("id_cep");
    const cepLimpo = input.value.replace(/\D/g, "");

    if (cepLimpo.length !== 8) return alert("CEP Inválido");

    try {
      btn_cep.disabled = true;
      const response = await fetch(`https://viacep.com.br/ws/${cepLimpo}/json/`);
      const data = await response.json();

      if (data.erro) throw new Error("CEP não encontrado.");

      fillFields(data, {
        id_uf: "uf",
        id_municipio: "localidade",
        id_codigo_municipio: "ibge",
        id_bairro: "bairro",
        id_logradouro: "logradouro",
      });
    } catch (error) {
      alert("Erro ao buscar CEP, tente mais tarde.");
      console.log(error.message);
    } finally {
      btn_cep.disabled = false;
    }
  });
}