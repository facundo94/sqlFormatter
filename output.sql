select
	concat(per_apellido,
	' ',
	per_nombres,
	' ',
	pd.perd_doc) as id,
	pd.perd_doc as dni,
	cast('gap' as varchar(10)) as origen,
	cast('vict/acus' as varchar(15)) as tipo,
	paises.pais_nac nacionalidad,
	edad_per.edad,
	cast(car_codigo as varchar(20)) as codigo,
	case when per.per_sexo=1
		then 'masculino'
		else case when per.per_sexo=2
		then 'femenino'
		else 'no declara' 
	end 
	end as per_sexo,
	c_per.carp_origtram,
	(1) as cantidad 
from zde_pm_tramites_integrados.caratula car 
inner join zde_pm_tramites_integrados.caratula_per c_per
	on ( c_per.carp_sumarionum = car.car_sumario
	and c_per.carp_sumarioanio = car.car_anio
	and c_per.carp_dep
	endencia = car.car_dep
	endencia
	and c_per.carp_tipo = car.car_tipo) 
inner join zde_pm_tramites_integrados.personas per
	on per.per_id=c_per.carp_per_id 
left join zde_pm_tramites_integrados.persona_doc pd
	on pd.perd_id=per.per_id 
left join temp_zdm_dim_ssso_sumarios_paises paises
	on paises.pais_id = per.per_nacionalidad 
left join temp_zdm_dim_ssso_sumarios_edad_personas edad_per
	on edad_per.per_id = per.per_id
where c_per.carp_origtram in (\0\,
	\1\,
	\2\)
	and car.sist_origen=2 
---------------------------------------------------------------
select
	concat(per_apellido,
	' ',
	per_nombres,
	' ',
	pd.perd_doc) as id,
	pd.perd_doc as dni,
	cast('gap' as varchar(10)) as origen,
	cast('vict/acus' as varchar(15)) as tipo,
	paises.pais_nac nacionalidad,
	edad_per.edad,
	cast(car_codigo as varchar(20)) as codigo,
	case when per.per_sexo=1
		then 'masculino'
		else case when per.per_sexo=2
		then 'femenino'
		else 'no declara' 
	end 
	end as per_sexo,
	c_per.carp_origtram,
	(1) as cantidad 
from zde_pm_tramites_integrados.caratula car 
inner join zde_pm_tramites_integrados.caratula_per c_per
	on ( c_per.carp_sumarionum = car.car_sumario
	and c_per.carp_sumarioanio = car.car_anio
	and c_per.carp_dep
	endencia = car.car_dep
	endencia
	and c_per.carp_tipo = car.car_tipo) 
inner join zde_pm_tramites_integrados.personas per
	on per.per_id=c_per.carp_per_id 
left join zde_pm_tramites_integrados.persona_doc pd
	on pd.perd_id=per.per_id 
left join temp_zdm_dim_ssso_sumarios_paises paises
	on paises.pais_id = per.per_nacionalidad 
left join temp_zdm_dim_ssso_sumarios_edad_personas edad_per
	on edad_per.per_id = per.per_id
where c_per.carp_origtram in (\0\,
	\1\,
	\2\)
	and car.sist_origen=2
---------------------------------------------------------------
