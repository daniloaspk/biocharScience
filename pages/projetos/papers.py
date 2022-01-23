import streamlit as st


def papers():
    text01 = "<h1 style='text-align: center; line-height: 1.15'>Publicações produzidas durante a vigência do " \
             "projeto</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    st.write("""
    ## Capítulos de livros
    """)

    text02 = "<p style='text-align: justify;'> SILVA, C. C.; SANTOS, D. A.; SILVA, A. G.; PASSOS, R. R.; RANGEL, " \
             "O. J. P.; SILVA, M. E. P. B.; PROFETI, D.; PROFETI, L. P. R. Biocarvões e disponibilidade de " \
             "fósforo para a produção vegetal. In: COSTA, A. V.; PARREIRA, L. A.;  PROFETI, L. P. R.; Campos, O. S." \
             " (Org.). Tópicos Especiais em Agroquímica I. 1 ed. Vitória: UFES, 2021, v. I, " \
             "p. 51-68. </p> "

    st.markdown(text02, unsafe_allow_html=True)

    st.write("""
        ## Artigos
        """)

    text03 = "<p style='text-align: justify;'> FONSECA, A.A.; SANTOS, D. A.; Moura Junior, C.D.; PASSOS, " \
             "R. R.; Rangel, O.J.P. Phosphorus and potassium in aggregates of degraded soils: changes caused by " \
             "biochar application. CLEAN (WEINHEIM. INTERNET), p. 2000366, 2021. </p> "

    st.markdown(text03, unsafe_allow_html=True)