select	(ROW_NUMBER() OVER()) AS seq
	,	zz.*
from	(
			select	z.account_id
				,	z.account_dt
				,	z.division_id
				,	z.division_nm
				, 	z.member_id
				,	z.member_nm
				,	z.payment_id
				,	z.payment_nm
				,	z.category_id
				,	z.category_nm
				,	z.category_seq
				,	cd.category_seq_nm
				,	z.price
				,	z.remark
				,	z.impulse_yn
			from	(
						select	a.account_id
							,	a.account_dt
							,	a.division_id
							,	d.division_nm
							,	a.member_id
							,	am.member_nm
							,	a.payment_id
							,	p.payment_nm
							,	c.category_nm
							,	a.price
							,	a.remark
							,	a.impulse_yn
							,	a.category_id
							,	a.category_seq
						from	account			a
							,	division		d
							,	account_member	am
							,	payment			p
							,	category		c
						where	1=1
						and		a.division_id 	= d.division_id
						and		a.member_id   	= am.member_id
						and		a.payment_id  	= p.payment_id
						and		a.category_id 	= c.category_id
						and		a.account_dt between %(strt_dt)s and %(end_dt)s
					) z
					left outer join category_dtl	cd
					on 		z.category_id 	= cd.category_id
					and		z.category_seq 	= cd.category_seq
			where	1=1
			order by z.account_dt desc
				,	 z.account_id desc
		) zz
where	1=1
;