delete
from	my_asset_accum
where	1=1
and		accum_dt = substring(%(procDt)s, 0, 7)
;