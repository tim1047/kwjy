select	dcm.division_id
	,	c.category_id
	,	c.category_nm
from	division_category_mpng	dcm
	,	category				c
where	1=1
and		dcm.category_id	= c.category_id
and		dcm.division_id = %(division_id)s
;