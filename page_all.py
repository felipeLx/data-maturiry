page_all = """
    <!doctype html>
    <html>
    <style>
        @import url('https://cdn.tailwindcss.com');
        @media screen {
            img {
                display: block;
            }
            }

            @media (max-width: 600px) {
            img {
                display: none;
            }
        }
    </style>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body>
        <div class="flex flex-col w-full">
            <img class="w-full h-[300px]" src="https://images2.imgbox.com/f3/43/aktnFlnv_o.png" style="object-fit: cover; border-radius: 8px; width: 100%; height: 100%;" alt="" />
            <div style="position: relative; flex-direction: column; widhth: 100%; font-size: 54px; font-weight: bold; justify-content: center;" class="flex-col w-full text-[54px] font-bold">Sua organização atingiu <span style="color:#00b7bd;"> {{formatted_median}} </span> de maturidade digital.&nbsp;</div>
            <br><br>
            <p style="font-size:24px; font-weight: normal; color:#292c2e; text-align: justify">Ficamos felizes em saber que a <span style="font-size:24px; font-weight:bold; color:#292c2e; text-align: justify">{{business}}</span> está avançando em sua jornada digital. Nesse relatório você vai encontrar um panorama geral dos pilares tecnológicos da sua empresa, e como avançar em cada um deles. Prepare-se para subir o nível de maturidade digital da sua empresa!&nbsp;</p>
            <br><br>
            <div style="font-size: 46px; font-weight: bold; text-align: center; justify-content: center;" class="text-2xl font-bold text-center justify-center">
                <span>Visão Geral</span>
            </div>
            <br><br>
            <div style="margin-bottom: 20px" class="mb-12">
            <ul class="space-y-2">
                <li style="display: flex; flex-direction: column; width: 100%; gap: 8px; text-align: left; margin-bottom: 4px; padding-bottom: 4px;" class="flex flex-col w-full gap-8 text-left mb-4 pb-4">
                <span style="text-align: left; font-size: 1.25rem; font-weight: bold; padding-bottom: 0.5rem; margin-bottom: 0.5rem;" class="text-left text-xl font-bold pb-2 mb-2">Infraestrutura</span>
                <div style="width: 100%; height: 10px; background-color: #8cf1f5; position: relative; padding: 2px; text-align: right;" class="bg-[#8cf1f5] relative h-[10px] w-full rounded-2xl">
                    <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_0}}%; border-radius: 0.5rem 0.5rem;" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_0}}%] rounded-2xl">
                        <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                        <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                        ></span>
                        {{value_0}}%
                        </span>
                    </div>
                    </div>
                </li>
                <li style="display: flex; flex-direction: column; width: 100%; gap: 8px; text-align: left; margin-bottom: 4px; padding-bottom: 4px;" class="flex flex-col w-full gap-8 text-left mb-4 pb-4">
                    <span style="text-align: left; font-size: 1.25rem; font-weight: bold; padding-bottom: 0.5rem; margin-bottom: 0.5rem;" class="text-left text-xl font-bold pb-2 mb-2">Ferramenta de Análise</span>
                    <div style="width: 100%; height: 10px; background-color: #8cf1f5; position: relative; padding: 2px; text-align: right;" class="bg-[#8cf1f5] relative h-[10px] w-full rounded-2xl">
                    <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_2}}%; border-radius: 0.5rem;" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_2}}%] rounded-2xl">
                        <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                        <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                        ></span>
                        {{value_2}}%
                        </span>
                    </div>
                    </div>
                </li>
                <li style="display: flex; flex-direction: column; width: 100%; gap: 8px; text-align: left; margin-bottom: 4px; padding-bottom: 4px;" class="flex flex-col w-full gap-8 text-left mb-4 pb-4">
                    <span style="text-align: left; font-size: 1.25rem; font-weight: bold; padding-bottom: 0.5rem; margin-bottom: 0.5rem;" class="text-left text-xl font-bold pb-2 mb-2">Gestão da Informação</span>
                    <div style="width: 100%; height: 10px; background-color: #8cf1f5; position: relative; padding: 2px; text-align: right;" class="bg-[#8cf1f5] relative h-[10px] w-full rounded-2xl">
                    <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_4}}%; border-radius: 0.5rem;" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_4}}%] rounded-2xl">
                        <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                        <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                        ></span>
                        {{value_4}}%
                        </span>
                    </div>
                    </div>
                </li>
                <li style="display: flex; flex-direction: column; width: 100%; gap: 8px; text-align: left; margin-bottom: 4px; padding-bottom: 4px;" class="flex flex-col w-full gap-8 text-left mb-4 pb-4">
                    <span style="text-align: left; font-size: 1.25rem; font-weight: bold; padding-bottom: 0.5rem; margin-bottom: 0.5rem;" class="text-left text-xl font-bold pb-2 mb-2">Gestão de Qualidade</span>
                    <div style="width: 100%; height: 10px; background-color: #8cf1f5; position: relative; padding: 2px; text-align: right;" class="bg-[#8cf1f5] relative h-[10px] w-full rounded-2xl">
                    <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_1}}%; border-radius: 0.5rem;" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_1}}%] rounded-2xl">
                        <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                        <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                        ></span>
                        {{value_1}}%
                        </span>
                    </div>
                    </div>
                </li>
                <li style="display: flex; flex-direction: column; width: 100%; gap: 8px; text-align: left; margin-bottom: 4px; padding-bottom: 4px;" class="flex flex-col w-full gap-8 text-left mb-4 pb-4">
                    <span style="text-align: left; font-size: 1.25rem; font-weight: bold; padding-bottom: 0.5rem; margin-bottom: 0.5rem;" class="text-left text-xl font-bold pb-2 mb-2">Análise de Dados</span>
                    <div style="width: 100%; height: 10px; background-color: #8cf1f5; position: relative; padding: 2px; text-align: right;" class="bg-[#8cf1f5] relative h-[10px] w-full rounded-2xl">
                    <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_3}}%; border-radius: 0.5rem;" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_3}}%] rounded-2xl">
                        <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                        <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                        ></span>
                        {{value_3}}%
                        </span>
                    </div>
                    </div>
                </li>
                <li style="display: flex; flex-direction: column; width: 100%; gap: 8px; text-align: left; margin-bottom: 4px; padding-bottom: 4px;" class="flex flex-col w-full gap-8 text-left mb-4 pb-4">
                    <span style="text-align: left; font-size: 1.25rem; font-weight: bold; padding-bottom: 0.5rem; margin-bottom: 0.5rem;" class="text-left text-xl font-bold pb-2 mb-2">Governança de Dados</span>
                    <div style="width: 100%; height: 10px; background-color: #8cf1f5; position: relative; padding: 2px; text-align: right;" class="bg-[#8cf1f5] relative h-[10px] w-full rounded-2xl">
                    <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_5}}%; border-radius: 0.5rem;" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_5}}%] rounded-2xl">
                        <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white; text-align: right" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white text-right">
                        <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10; text-align: right" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm text-right"
                        ></span>
                        {{value_5}}%
                        </span>
                    </div>
                    </div>
                </li>
            </ul>
            </div>
            <br />
            <div class="pt-[80px]"></div>
            <p class="pb-4 mb-4" style="font-size:40px; font-weight:bold; color:#292c2e; padding:4px; text-align:center">Infraestrutura de Dados: 
            <div style="width: 100%; height: 30px; background-color: #8cf1f5; position: relative; padding: 2px;" class="bg-[#8cf1f5] relative h-[30px] w-full rounded-2xl">
                <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_0}}%; border-radius: 0.5rem; text-align: right" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_0}}%] rounded-2xl">
                    <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                    <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                    ></span>
                    {{value_0}}%
                    </span>
                </div>
            </div>
            <div class="pt-[20px]"></div>
            <div class="mt-2 pt-2" style="text-align:left; margin-top: 2px; padding-top: 2px">
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">A infraestrutura refere-se à base de trabalho, física e tecnológica, que suporta o armazenamento, processamento e acesso a dados em uma organização. Isso envolve servidores, redes, sistemas de armazenamento, bancos de dados e outras tecnologias que permitem a coleta, armazenamento seguro e eficiente, processamento e disponibilização de dados para os usuários e sistemas que deles necessitam. Uma estação sólida de trabalho é crucial para garantir a segurança e integridade dos dados, bem como as entregas e a disponibilidade de informações para a gestão.&nbsp;</span>
                <br><br>
                <div style="width: 100%; height: auto;  place-items: center; margin: 48px 0 12px 0;">
                    <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left">Como está hoje</span>
                </div>
                <br><br>
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{today_0}}</span>
                <br><br>
                <div style="width: 100%; height: auto; place-items: center; margin: 48px 0 12px 0;">
                    <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left">Como pode melhorar</span>
                </div>
                <br><br>
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{future_0}}</span>
                <br><br>
            </div>
            <br />
            <div class="pt-[80px]"></div>
            <p class="pb-4 mb-4" style="font-size:40px; font-weight:bold; color:#292c2e; padding:4px; text-align:center">Gestão de Qualidade de Dados: 
            <div style="width: 100%; height: 30px; background-color: #8cf1f5; position: relative; padding: 2px;" class="bg-[#8cf1f5] relative h-[30px] w-full rounded-2xl">
                <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_1}}%; border-radius: 0.5rem; text-align: right" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_1}}%] rounded-2xl">
                    <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                    <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                    ></span>
                    {{value_1}}%
                    </span>
                </div>
            </div>
            <div class="pt-[20px]"></div>
            <div class="mt-2 pt-2" style="text-align:left; margin-top: 2px; padding-top: 2px">
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">A gestão da qualidade se refere a um conjunto de práticas, processos e profissionais técnicos voltados para garantir que seus produtos, serviços ou processos atendam aos padrões e expectativas estabelecidos.&nbsp;</span>
                <br><br>
                <div style="width: 100%; height: auto;  place-items: center;  margin: 48px 0 12px 0;">
                    <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left">Como está hoje</span>
                </div>
                <br><br>
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{today_1}}</span>
                <br><br>
                <div style="width: 100%; height: auto; place-items: center;  margin: 48px 0 12px 0;">
                    <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left;">Como pode melhorar</span>
                </div>
                <br><br>
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{future_1}}</span>
                <br><br>
            </div>
            <br />
            <div class="pt-[80px]"></div>
            <p class="pb-4 mb-4" style="font-size:40px; font-weight:bold; color:#292c2e; padding:4px; text-align:center">Ferramenta de Análise: 
            <div style="width: 100%; height: 30px; background-color: #8cf1f5; position: relative; padding: 2px;" class="bg-[#8cf1f5] relative h-[30px] w-full rounded-2xl">
                <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_2}}%; border-radius: 0.5rem; text-align: right" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_2}}%] rounded-2xl">
                    <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                    <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                    ></span>
                    {{value_2}}%
                    </span>
                </div>
            </div>
            <div class="pt-[20px]"></div>
            <div class="mt-2 pt-2" style="text-align:left; margin-top: 2px; padding-top: 2px">
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">As ferramentas de gestão de serviços ou de dados são softwares ou plataformas utilizadas para facilitar requisições, coletar dados, transformar processos, visualizar e interpretar insights significativos via relatórios. Essas ferramentas podem variar desde simples planilhas até sistemas mais avançados, como Business Intelligence (BI), softwares ITSM, CRM ou ERP. Elas permitem que as organizações explorem os dados, identifiquem padrões, façam previsões e tomem decisões informadas.&nbsp;</span>
                <br><br>
                <div style="width: 100%; height: auto;  place-items: center; margin: 48px 0 12px 0;">
                    <span style="font-size:20px;  font-weight:bold; color:#292c2e; text-align:left">Como está hoje</span>
                </div>
                <br><br>
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{today_2}}</span>
                <br><br>
                <div style="width: 100%; height: auto; place-items: center; margin: 48px 0 12px 0;">
                    <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left">Como pode melhorar</span>
                </div>
                <br><br>
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{future_2}}</span>
                <br><br>
            </div>
            <br />
            <div class="pt-[80px]"></div>
            <p class="pb-4 mb-4" style="font-size:40px; font-weight:bold; color:#292c2e; padding:4px; text-align:center">Análise de Dados: 
            <div style="width: 100%; height: 30px; background-color: #8cf1f5; position: relative; padding: 2px;" class="bg-[#8cf1f5] relative h-[30px] w-full rounded-2xl">
                <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_3}}%; border-radius: 0.5rem; text-align: right" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_3}}%] rounded-2xl">
                    <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                    <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                    ></span>
                    {{value_3}}%
                    </span>
                </div>
            </div>
            <div class="pt-[20px]"></div>
            <div class="mt-2 pt-2" style="text-align:left; margin-top: 2px; padding-top: 2px">
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">A análise de dados é o processo de examinar, limpar, transformar e interpretar conjuntos de dados para identificar padrões, tendências, relações e insights relevantes. A análise de dados é frequentemente usada como base para a tomada de decisões informadas em uma organização. Ela permite que os gestores e profissionais examinem as informações disponíveis, compreendam as implicações das tendências e façam escolhas embasadas em evidências. Uma análise de dados sólida contribui para a redução de incertezas e riscos nas decisões empresariais, levando a melhores resultados.&nbsp;</span>
                <br><br>
                <div style="width: 100%; height: auto;  place-items: center; margin: 48px 0 12px 0;">
                    <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left">Como está hoje</span>
                </div>
                <br><br>
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{today_3}}</span>
                <br><br>
                <div style="width: 100%; height: auto; place-items: center; margin: 48px 0 12px 0;">
                    <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left">Como pode melhorar</span>
                </div>
                <br><br>
                <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{future_3}}</span>
                <br><br>
            </div>
        <br />
        <div class="pt-[80px]"></div>
        <p class="pb-4 mb-4" style="font-size:40px; font-weight:bold; color:#292c2e; padding:4px; text-align:center">Gestão da Informação: 
        <div style="width: 100%; height: 30px; background-color: #8cf1f5; position: relative; padding: 2px;" class="bg-[#8cf1f5] relative h-[30px] w-full rounded-2xl">
                <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_4}}%; border-radius: 0.5rem; text-align: right" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_4}}%] rounded-2xl">
                    <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                    <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                    ></span>
                    {{value_4}}%
                    </span>
                </div>
            </div>
            <div class="pt-[20px]"></div>
        <div class="mt-2 pt-2" style="text-align:left; margin-top: 2px; padding-top: 2px">
            <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">A gestão da informação envolve o processo de coleta, organização, armazenamento, recuperação e distribuição de informações de maneira eficiente e eficaz. A criação de procedimentos padrões, os ajustes de processos da área, a definição de um catálogo de serviços e a redefinição de prioridades garante que as informações sejam capturadas de forma precisa, estejam disponíveis quando necessário e sejam mantidas de maneira segura. Além disso, elas podem ser acessadas e compartilhadas de maneira colaborativa por toda a organização.&nbsp;</span>
            <br><br>
            <div style="width: 100%; height: auto;  place-items: center;  margin: 48px 0 12px 0;">
                <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left">Como está hoje</span>
            </div>
            <br><br>
            <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{today_4}}</span>
            <br><br>
            <div style="width: 100%; height: auto; place-items: center; margin: 48px 0 12px 0;">
                <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left">Como pode melhorar</span>
            </div>
            <br><br>
            <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{future_4}}</span>
            <br><br>
        </div>
        <br />
        <div class="pt-[80px]"></div>
        <p class="pb-4 mb-4" style="font-size:40px; font-weight:bold; color:#292c2e; padding:4px; text-align:center">Governança de Dados: 
        <div style="width: 100%; height: 30px; background-color: #8cf1f5; position: relative; padding: 2px;" class="bg-[#8cf1f5] relative h-[30px] w-full rounded-2xl">
            <div style="background-color: #00b7bd; position: absolute; top: 0; left: 0; height: 100%; width: {{value_5}}%; border-radius: 0.5rem; text-align: right" class="bg-[#00b7bd] absolute top-0 left-0 h-full w-[{{value_5}}%] rounded-2xl">
                <span style="background-color: #00b7bd; position: absolute; right: -4px; bottom: 0; margin-bottom: 2px; border-radius: 0.25rem; padding: 1px 2px; font-size: 0.75rem; font-weight: 600; color: white;" class="bg-[#00b7bd] absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-semibold text-white">
                <span style="background-color: #00b7bd; position: absolute; bottom: -2px; left: 50%; transform: translateX(-50%) rotate(45deg); height: 2px; width: 2px; border-radius: 0.25rem; z-index: -10;" class="bg-[#00b7bd] absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"
                ></span>
                {{value_5}}%
                </span>
            </div>
        </div>
        <div class="pt-[20px]"></div>
        <div class="mt-2 pt-2" style="text-align:left; margin-top: 2px; padding-top: 2px">
            <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">A governança de TI refere-se ao conjunto de políticas, processos, padrões e controles que garantem a qualidade, segurança, conformidade e uso responsável dos dados dentro de uma organização. Definir processos, documentos centralizados e controle do andamento de solicitações visa estabelecer responsabilidades claras para a gestão, uso e proteção dos dados, e conformidades garantidas. Quando focada em dados, também abrange a definição de metadados, a criação de regras para aquisição e integração de dados, a manutenção da consistência e a resolução de conflitos.&nbsp;</span>
            <br><br>
            <div style="width: 100%; height: auto;  place-items: center; margin: 48px 0 12px 0;">
                <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left">Como está hoje</span>
            </div>
            <br><br>
            <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{today_5}}</span>
            <br><br>
            <div style="width: 100%; height: auto; place-items: center; margin: 48px 0 12px 0;">
                <span style="font-size:20px; font-weight:bold; color:#292c2e; text-align:left">Como pode melhorar</span>
            </div>
            <br><br>
            <span style="font-size:16px; font-weight: normal; color:#292c2e; text-align:justify">{{future_5}}</span>
            <br><br>
        </div>
    </body>
</html>
"""