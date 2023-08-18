from app.base_models import FiltrosRelatorio
from app.services import RelatorioPesquisaAvancada

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, FileResponse


router = APIRouter(prefix="/user", tags=["User"])
relatorio = RelatorioPesquisaAvancada()

@router.post("/extrair_relatorio_empresarial")
async def extrair_relatorio(data: FiltrosRelatorio):
    try:
        filtros = data.dict()
        pesquisa = await relatorio.buscar_cnpjs(filtros)

        if not pesquisa:
            return JSONResponse(
            content=jsonable_encoder(
                {"message": "Não foi possível gerar o relatório, verifique os filtros e tente novamente."}
            ),
            status_code=status.HTTP_400_BAD_REQUEST
        )

        return FileResponse(
            path=pesquisa,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            filename=pesquisa,
            status_code=status.HTTP_201_CREATED
        )

    except Exception as error:
        print(error)
        return JSONResponse(
            content=jsonable_encoder(
                {"message": "Não foi possível gerar o relatório, verifique os filtros e tente novamente."}
            ),
            status_code=status.HTTP_400_BAD_REQUEST
        )