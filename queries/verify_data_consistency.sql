select job_title
from hr.jobs j
join hr.employees e on e.job_id = j.job_id
where e.manager_id IS NULL
