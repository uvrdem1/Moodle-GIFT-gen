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


  const downloadGift = (
    item: HistoryItem
  ) => {

    const blob = new Blob(
      [item.result],
      {
        type: 'text/plain'
      }
    )

    const url =
      window.URL.createObjectURL(
        blob
      )

    const link =
      document.createElement('a')

    link.href = url

    link.download =
      `${item.topic}.gift`

    link.click()

    window.URL.revokeObjectURL(
      url
    )
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
              className="bg-slate-900 p-6 rounded-2xl border border-slate-800"
            >

              <div className="flex items-center justify-between mb-4">

                <div>

                  <h2 className="text-2xl font-semibold">
                    {item.topic}
                  </h2>

                  <p className="text-slate-400 mt-1">
                    {
                      new Date(
                        item.created_at
                      ).toLocaleString()
                    }
                  </p>

                </div>


                <button
                  onClick={() =>
                    downloadGift(item)
                  }
                  className="bg-blue-600 hover:bg-blue-500 transition-all px-5 py-3 rounded-xl"
                >
                  Скачать .gift
                </button>

              </div>


              <pre className="whitespace-pre-wrap text-sm bg-slate-950 p-4 rounded-xl overflow-auto">
                {item.result}
              </pre>

            </div>
          ))
        }

      </div>

    </div>
  )
}