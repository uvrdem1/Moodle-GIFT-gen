import { useEffect, useState } from 'react'

import api from '../api'


interface HistoryItem {

  id: number

  topic: string

  result: string

  created_at: string
}


export default function History() {

  const [history, setHistory] =
    useState<HistoryItem[]>([])


  useEffect(() => {

    fetchHistory()

  }, [])


  const fetchHistory = async () => {

    try {

      const response = await api.get(
        '/history/'
      )

      setHistory(response.data)

    } catch (error) {

      console.error(error)
    }
  }


  return (

    <div className="min-h-screen bg-slate-950 text-white p-10">

      <h1 className="text-4xl font-bold mb-8">
        История генераций
      </h1>

      <div className="space-y-6">

        {
          history.map((item) => (

            <div
              key={item.id}
              className="bg-slate-900 p-6 rounded-2xl"
            >

              <h2 className="text-2xl font-semibold mb-3">
                {item.topic}
              </h2>

              <p className="text-slate-400 mb-4">
                {
                  new Date(
                    item.created_at
                  ).toLocaleString()
                }
              </p>

              <pre className="whitespace-pre-wrap text-sm">
                {item.result}
              </pre>

            </div>
          ))
        }

      </div>

    </div>
  )
}