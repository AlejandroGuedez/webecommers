import useSWR from 'swr'
import { useEffect } from 'react'

const fetcher = (url: string) => fetch(url).then(res => res.json())

export default function Home() {
  const { data } = useSWR('http://backend:8000/products', fetcher)
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Storefront Demo</h1>
      <ul>
        {data?.map((p:any) => (
          <li key={p.id}>{p.title}</li>
        ))}
      </ul>
    </div>
  )
}
